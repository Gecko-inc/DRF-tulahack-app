from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserStatus(models.Model):
    title = models.CharField(_("Название"), max_length=130)

    class Meta:
        verbose_name = _("Статус пользователя")
        verbose_name_plural = _("Статусы пользователей")

    def __str__(self):
        return self.title


class User(AbstractUser, UserManager):
    status = models.ForeignKey(UserStatus, verbose_name=_("Статус"), on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username + " | " + str(self.status)


class MobileUser(models.Model):
    token = models.CharField(_("Токен"), max_length=130, unique=True)
    date_joined = models.DateTimeField(_('Дата регистрации'), default=timezone.now)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи мобильного приложения")

    def __str__(self):
        return self.token


class Bookmark(models.Model):
    user = models.ForeignKey(MobileUser, on_delete=models.CASCADE, related_name='bookmarks')
    article = models.ForeignKey("section.Article", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Закладка")
        verbose_name_plural = _("Закладки")

    def __str__(self):
        return f"{self.id}"

    def info(self) -> dict:
        return {
            "section_id": self.article.section.id,
            "article_id": self.article.id,
        }
