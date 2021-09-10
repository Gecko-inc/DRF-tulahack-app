from django.db import models
from django.utils.translation import gettext_lazy as _


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
