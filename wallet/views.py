import os

from rest_framework.views import APIView
from rest_framework.response import Response
from config.views import init_user
from .core import gen_address, create_qr
from .models import Wallet
from django.core.files import File
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import WalletSerializer


class WalletView(APIView):
    # TODO: получене одного кошелька из query
    # TODO: PATH запрос на редактирование label
    @swagger_auto_schema(tags=['Wallet'])
    def get(self, request):
        user = init_user(request)
        wallets = Wallet.objects.filter(user=user)
        return Response(WalletSerializer(wallets, many=True).data, status=201)

    @swagger_auto_schema(tags=['Wallet'])
    def post(self, request):
        user = init_user(request)
        data = request.data
        Wallet.objects.all()
        result = gen_address(Wallet.objects.last().id + 1)
        img_path = create_qr(result[0])
        wallet = Wallet.objects.create(
            user=user,
            label=data.get("label", 'BTC wallet'),
            address=result[0],
            wif=result[1],
            qr_code=File(open(img_path, 'rb'))

        )
        os.remove(img_path)
        return Response(WalletSerializer(wallet, many=False).data, status=201)

    @swagger_auto_schema(tags=['Wallet'],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['wallet_id'],
                             properties={
                                 'wallet_id': openapi.Schema(type=openapi.TYPE_INTEGER)
                             },
                         ),
                         )
    def delete(self, request):
        user = init_user(request)
        data = request.data
        try:
            Wallet.objects.get(id=data.get("wallet_id"), user=user).delete()
        except Wallet.DoesNotExist:
            pass

        return Response(status=201)


class TransactionView(APIView):
    # TODO: POST запрос на создание транзакции
    # TODO: GET запрос на просмотр статуса транзакции
    ...
