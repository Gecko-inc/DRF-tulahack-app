from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Название"), max_length=130)
    user = models.ForeignKey("account.User", verbose_name=_("Пользователь"), blank=True, null=True,
                             on_delete=models.SET_NULL, related_name="user_category")
    icon = models.CharField(_("Иконка категории"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.title


class Expenses(models.Model):
    user = models.ForeignKey("account.User", verbose_name=_("Пользователь"), on_delete=models.CASCADE,
                             related_name="user_expenses")
    category = models.CharField(_("Категория"), default="Оплата товаров и услуг", max_length=210)
    title = models.CharField(_("Название"), max_length=130)
    money = models.FloatField(_("Сумма"))
    date = models.DateField(_("Дата"), default=timezone.now().date())

    class Meta:
        verbose_name = _("Расход")
        verbose_name_plural = _("Расходы")
        ordering = ["category", 'date']

    def __str__(self):
        return f"{self.title}| {self.money} RUB"


class Income(models.Model):
    title = models.CharField(_("Название"), max_length=130)
    user = models.ForeignKey("account.User", verbose_name="Пользователь", on_delete=models.CASCADE, null=True,
                             related_name="user_income")
    money = models.FloatField(_("Сумма"))
    date = models.DateField(_("Дата"), default=timezone.now().date())

    class Meta:
        verbose_name = _("Доход")
        verbose_name_plural = _("Доходы")
        ordering = ['date']

    def __str__(self):
        return f"{self.title}| {self.money} RUB"
