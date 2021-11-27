from django.urls import path
from .views import ExpensesView

app_name = "finance"

urlpatterns = [
    path("expenses/", ExpensesView.as_view(), name="Expenses")
]
