import random

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    def get(self, request):
        pass
