from django.urls import path
from .views import *

app_name = "fitness"

urlpatterns = [
    path('user-exercises/', UserFitnessView.as_view(), name="user-exercises"),
    path('exercises/', ExerciseView.as_view(), name="exercises"),

]
