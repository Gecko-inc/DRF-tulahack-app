from django.urls import path, re_path
from account.views import *

app_name = "account"

urlpatterns = [
    re_path(r'^month-expenses/(?P<month>\d{1,2})', GetUserMonthExpenses.as_view(), name="month-expenses"),
    re_path(r'^month-steps/(?P<month>\d{1,2})', GetUserMonthSteps.as_view(), name="month-expenses"),
]
