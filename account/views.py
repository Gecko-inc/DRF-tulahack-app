from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializer import UserSerializer
from config.views import init_user


class GetUserMonthExpenses(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Custom-User"], operation_description="Token required")
    def get(self, request, *args, **kwargs):
        return Response(
            User.objects.get(id=init_user(request).id).get_last_month_expenses(kwargs.get('month', datetime.month)))


class GetUserMonthSteps(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Custom-User"], operation_description="Token required")
    def get(self, request, *args, **kwargs):
        return Response(
            User.objects.get(id=init_user(request).id).get_last_month_steps(kwargs.get('month', datetime.month)))


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Custom-User'], operation_description="Token required")
    def get(self, request):
        user = init_user(request)
        return Response(UserSerializer(user, many=False).data, status=201)

    @swagger_auto_schema(tags=['Custom-User'],
                         operation_description="Обновление лимита средств, цель шагов, изображения пользователя\nToken required",
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['id'],
                             properties={
                                 'step_target': openapi.Schema(type=openapi.TYPE_INTEGER),
                                 'money_limit': openapi.Schema(type=openapi.TYPE_STRING),
                             },
                         ),
                         )
    def put(self, request):
        user = init_user(request)
        data = request.data
        if data.get("money_limit"):
            try:
                money = float(data.get("money_limit"))
            except (ValueError, TypeError):
                return Response({"error": "Invalid data"}, status=400)

            user.money_limit = money

        user.step_target = data.get("step_target", user.step_target)
        if data.get("image"):
            # TODO: check it!
            # Hello Backend Developer who did this
            # I have several questions. Why blyat do you leave except: pass in your code
            try:
                user.image = data.get("image")
            except (ValueError, ValidationError, Exception) as e:
                print(e)
        user.save()
        return Response(UserSerializer(user, many=False).data, status=201)
