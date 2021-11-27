from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from config.views import init_user


class GetUserMonthExpenses(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["User"], operation_description="Token required")
    def get(self, request, *args, **kwargs):
        return Response(
            User.objects.get(id=init_user(request).id).get_last_month_expenses(kwargs.get('month', datetime.month)))


class GetUserMonthSteps(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["User"], operation_description="Token required")
    def get(self, request, *args, **kwargs):
        return Response(
            User.objects.get(id=init_user(request).id).get_last_month_steps(kwargs.get('month', datetime.month)))
