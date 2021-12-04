from django.db import models
import requests
from bit import PrivateKey

from config.views import get_upload_to


class Wallet(models.Model):
    user = models.ForeignKey("account.User", related_name="wallet", on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    label = models.CharField("Название", max_length=130)
    address = models.CharField("Адрес", max_length=210)
    wif = models.CharField("WIF", max_length=210)
    qr_code = models.ImageField("QR", upload_to=get_upload_to)

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"

    def __str__(self):
        return self.label

    @property
    def txh(self) -> list:
        """
          Возвращает список всех транзакций
        """
        url = f'https://blockchain.info/rawaddr/{self.address}'
        x = requests.get(url)
        result = x.json()
        return result['txs']

    @property
    def balance(self) -> str:
        key = PrivateKey(wif=self.wif)
        return key.get_balance()
