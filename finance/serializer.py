from rest_framework import serializers
from .models import Expenses, Category, Income


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = [
            "id",
            'title',
            'category_name',
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
