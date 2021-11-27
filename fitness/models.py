from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import AbsSort


class Exercise(models.Model):
    title = models.CharField(_("Название упражнения"), max_length=255, blank=True)
    description = models.TextField(_("Описание упражнения"), blank=True)

    class Meta:
        verbose_name = _("Упражнение")
        verbose_name_plural = _("Упражнения")


class UserFitness(AbsSort):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name="fitness",
                             verbose_name=_("Пользователь"))
    unit = models.CharField(_("Мера измерения"), max_length=20, default="м")
    exercise = models.ForeignKey("fitness.Exercise", on_delete=models.SET_NULL, related_name="fitness",
                                 verbose_name=_("Упражнение"))
    progress = models.PositiveIntegerField(_("Прогресс упражнения"))
    is_current = models.BooleanField(_("Текущее упражнение"), default=False)

    class Meta:
        verbose_name = _("Фитнес-трекер пользователя")
        verbose_name_ = _("Фитнес-трекер пользователей")
