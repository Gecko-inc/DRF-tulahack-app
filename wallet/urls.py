from django.urls import path
from .views import WalletView

app_name = "finance"

urlpatterns = [
    path("wallet/", WalletView.as_view(), name="wallet"),
]
