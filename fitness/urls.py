from django.urls import path
from .views import *

app_name = "fitness"

urlpatterns = [
    path('user-exercises/', GetUserFitness.as_view(), name="user-exercises"),
]
