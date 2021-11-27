from django.contrib import admin
from .models import Expenses, Category


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
