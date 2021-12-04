from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            'label',
            'address',
            'qr_code',
            'balance',
            'txh',
        ]
