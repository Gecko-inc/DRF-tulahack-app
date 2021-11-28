from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'image',
            'balance',
            'money_limit',
            'step_target',
            'get_last_month_expenses',
            'get_last_month_income',
            'get_last_month_steps',
            'current_exercise',
        ]
