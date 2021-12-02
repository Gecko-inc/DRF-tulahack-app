from django.db import models

from config.models import AbsCreated, AbsAccount
from django.utils.translation import gettext_lazy as _


class Todo(AbsAccount, AbsCreated):
    title = models.CharField(_("Наименование задания"), max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("TODO-лист")
        verbose_name_plural = _("TODO-листы")
