from django.urls import path
from .views import StepView

app_name = "step"

urlpatterns = [
    path("step/", StepView.as_view(), name="step")
]
