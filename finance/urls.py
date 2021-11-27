from django.urls import path
from .views import ExpensesView, CategoryView, IncomeView

app_name = "finance"

urlpatterns = [
    path("expenses/", ExpensesView.as_view(), name="Expenses"),
    path("income/", IncomeView.as_view(), name="Income"),
    path("category/", CategoryView.as_view(), name="category")
]
