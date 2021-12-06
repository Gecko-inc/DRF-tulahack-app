from django.urls import path
from .views import WalletView, TransactionView

app_name = "finance"

urlpatterns = [
    path("wallet/", WalletView.as_view(), name="wallet"),
    path("transaction/", TransactionView.as_view(), name="transaction"),
]
