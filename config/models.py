from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_template import settings


class Config(models.Model):
    title = models.CharField(_("Наименование"), max_length=130)
    description = models.TextField(_("Описание"), blank=True)
    key = models.CharField(_("Ключ"), max_length=130, unique=True)
    value = models.CharField(_("Значение"), blank=True, max_length=210)

    class Meta:
        verbose_name = _("Настройка")
        verbose_name_plural = _("Найстройки")

    def __str__(self):
        return self.title

    @classmethod
    def get_cfg(cls) -> dict:
        """
          returns a dict of text settings
        """
        context = dict((cfg.key, cfg.value) for cfg in cls.objects.all())

        return context


class AbsSort(models.Model):
    sort = models.IntegerField(_("Сортировка"), default=0)

    class Meta:
        abstract = True


class AbsCreated(models.Model):
    created = models.DateTimeField(_("Дата создания"), default=timezone.now)

    class Meta:
        abstract = True


class AbsAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь"))

    class Meta:
        abstract = True
