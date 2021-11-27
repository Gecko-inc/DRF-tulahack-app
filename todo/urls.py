from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', TodoView.as_view(), name="todo"),
]
