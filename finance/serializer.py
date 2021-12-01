from rest_framework import serializers
from .models import Expenses, Category, Income


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = [
            "id",
            'title',
            'category',
            'money',
            'date'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title"
        ]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            "id",
            "title",
            "money",
            "date"
        ]
