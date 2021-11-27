from django.urls import path

from covid.views import CovidView

urlpatterns = [
    path('check-covid/', CovidView.as_view(), name="check-covid"),
]
