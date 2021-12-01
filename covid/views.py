from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


def parse(url: str):
    import requests
    import re
    from datetime import datetime
    if url:
        ck = re.findall("ck\=(\S+)", url)
        print("Getting params:")
        params = (('lang', 'ru'), ('ck', ck),)
        if len(ck):
            print(f"ck={ck}")
            print("Getting numbers: ")
            numbers = re.findall("[\/](\d+)", url)
            print(f"numbers={numbers}")
            print("Making request")
            if len(numbers):
                url = "https://www.gosuslugi.ru/api/covid-cert/v3/cert/check/" + str(numbers[0])
                response = requests.get(url, params=params)
                unformatted_date = re.findall("\"expiredAt\"\:\"([\d+\.]+)\"", response.text)
                if len(unformatted_date):
                    date = datetime.strptime(unformatted_date[0], "%d.%m.%Y")
                    if date and date > datetime.now():
                        return "С этим человеком можно здороваться"
    return "С этим человеком лучше не общаться"


class CovidView(APIView):
    @swagger_auto_schema(tags=["Covid"],
                         operation_description="Получение информации о ковидной прививке человека",
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=["url"],
                             properties={
                                 "url": openapi.Schema(type=openapi.TYPE_STRING)
                             }
                         ))
    def post(self, request, *args, **kwargs):
        url = request.data.get('url', None)
        return Response(parse(url), status=200)
