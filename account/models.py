from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, UserManager):
    image = models.ImageField(_("Аватар пользователя"), blank=True, null=True, upload_to="user/image")
    balance = models.FloatField(_("Баланс"), default=0.00)
    money_limit = models.FloatField(_("Денежный лимит"), default=30000.00)
    step_target = models.IntegerField(_("Цель по шагам"), default=10000)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username

    def update_balance(self, money: float) -> float:
        self.balance += money
        self.save()
        return self.balance
