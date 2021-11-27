from django.urls import path
from .views import ExpensesView, CategoryView

app_name = "finance"

urlpatterns = [
    path("expenses/", ExpensesView.as_view(), name="Expenses"),
    path("category/", CategoryView.as_view(), name="category")
]
