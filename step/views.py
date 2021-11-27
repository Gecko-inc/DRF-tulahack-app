from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from config.views import init_user
from step.models import Step
from step.serializer import StepSerializer


class StepView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Finance'])
    def get(self, request):
        user = init_user(request)
        try:
            step = Step.objects.get(date=timezone.now, user=user)
        except Step.DoesNotExist:
            step = Step.objects.create(user=user)

        return Response(StepSerializer(step, many=False).data, status=201)

    @swagger_auto_schema(tags=['Finance'],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['count'],
                             properties={
                                 'count': openapi.Schema(type=openapi.TYPE_INTEGER)
                             },
                         ),
                         )
    def post(self, request):
        user = init_user(request)
        try:
            step = Step.objects.get(date=timezone.now, user=user)
        except Step.DoesNotExist:
            step = Step.objects.create(user=user)

        step.count = request.data.get("count")

        return Response(StepSerializer(step, many=False).data, status=201)
