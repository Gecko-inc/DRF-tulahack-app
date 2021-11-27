from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Название"), max_length=130)
    user = models.ForeignKey("account.User", verbose_name=_("Пользователь"), blank=True, null=True,
                             on_delete=models.SET_NULL, related_name="user_category")

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.title


class Expenses(models.Model):
    user = models.ForeignKey("account.User", verbose_name=_("Пользователь"), on_delete=models.CASCADE,
                             related_name="user_expenses")
    category = models.ForeignKey(Category, verbose_name=_("Категория"), on_delete=models.CASCADE)
    title = models.CharField(_("Название"), max_length=130)
    money = models.DecimalField(_("Сумма"), max_digits=12, decimal_places=2)
    date = models.DateField(_("Дата"), default=timezone.now)

    class Meta:
        verbose_name = _("Расход")
        verbose_name_plural = _("Расходы")
        ordering = ["category", 'date']

    def __str__(self):
        return f"{self.title}| {self.money} RUB"


class Income(models.Model):
    title = models.CharField(_("Название"), max_length=130)
    money = models.DecimalField(_("Сумма"), max_digits=12, decimal_places=2)
    date = models.DateField(_("Дата"), default=timezone.now)

    class Meta:
        verbose_name = _("Доход")
        verbose_name_plural = _("Доходы")
        ordering = ['date']

    def __str__(self):
        return f"{self.title}| {self.money} RUB"
