from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, UserManager):
    image = models.ImageField(_("Аватар пользователя"), blank=True, null=True, upload_to="user/image")
    money_limit = models.DecimalField(_("Денежный лимит"), decimal_places=2, max_digits=12, default=30000.00)
    step_target = models.IntegerField(_("Цель по шагам"), default=10000)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username
