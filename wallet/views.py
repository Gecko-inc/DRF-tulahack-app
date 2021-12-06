import os

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from config.views import init_user
from .core import gen_address, create_qr, send_btc
from .models import Wallet
from django.core.files import File
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import WalletSerializer


class WalletView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['Wallet'],
        manual_parameters=[
            openapi.Parameter('wallet_id', openapi.IN_PATH, description='ID кошелька.',
                              required=True,
                              type=openapi.TYPE_INTEGER)
        ]
    )
    def get(self, request):
        user = init_user(request)
        data = request.GET
        if data.get("wallet_id"):
            try:
                wallet = Wallet.objects.get(user=user, id=data.get("wallet_id"))
                return Response(WalletSerializer(wallet, many=False).data, status=201)
            except Wallet.DoesNotExist:
                return Response({"error": "Wallet does not exist"}, status=404)
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

    @swagger_auto_schema(tags=['Wallet'],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['wallet_id'],
                             properties={
                                 'wallet_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                 'label': openapi.Schema(type=openapi.TYPE_STRING),
                             },
                         ),
                         )
    def path(self, request):
        user = init_user(request)
        data = request.data
        try:
            wallet = Wallet.objects.get(id=data.get("wallet_id"), user=user)
            wallet.label = data.get("label", wallet.label)
            wallet.save()
            return Response(WalletSerializer(wallet, many=False).data, status=201)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet does not exist"}, status=404)


class TransactionView(APIView):
    permission_classes = [IsAuthenticated]
    # TODO: GET запрос на просмотр статуса транзакции

    @swagger_auto_schema(tags=['Transaction'],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['wallet_id'],
                             properties={
                                 'wallet_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                 'amount': openapi.Schema(type=openapi.TYPE_STRING),
                                 'address': openapi.Schema(type=openapi.TYPE_STRING),
                             },
                         ),
                         )
    def post(self, request):
        user = init_user(request)
        data = request.data
        try:
            amount = float(data.get("amount"))
        except (ValueError, TypeError):
            return Response({"error": "Invalid data"}, status=400)
        try:
            wallet = Wallet.objects.get(id=data.get("wallet_id"), user=user)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet does not exist"}, status=404)
        result = send_btc(wallet, amount, data.get("address"))
        if result == 'success':
            return Response({
                "message": result
            }, status=201)

        return Response({
            "error": result
        }, status=400)
