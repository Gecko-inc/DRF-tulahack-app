from django.db import models
from django.utils.translation import gettext_lazy as _

from config.views import get_upload_to


class Section(models.Model):
    title = models.CharField(_("Заголовок"), max_length=130)
    sort = models.IntegerField(_("Сортировка"), default=0)
    is_active = models.BooleanField(_("Активна"), default=True)

    class Meta:
        verbose_name = _("Раздел")
        verbose_name_plural = _("Разделы")
        ordering = ['-sort', ]

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(_("Заголовок"), max_length=130)
    section = models.ForeignKey(Section, verbose_name=_("Раздел"), on_delete=models.SET_NULL, null=True,
                                related_name="articles", blank=True)
    sort = models.IntegerField(_("Сортировка"), default=0)
    is_active = models.BooleanField(_("Активна"), default=True)

    class Meta:
        ordering = ['-sort', ]
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

    def __str__(self):
        return self.title


class ArticleMedia(models.Model):
    IMAGE_PATH = "sections/article"

    article = models.ForeignKey(Article, verbose_name=_("Статья"), on_delete=models.CASCADE, related_name="detail")
    text = models.TextField(_("Текст"), null=True)
    additional_text = models.TextField("Сноска", blank=True, null=True)
    word = models.TextField("Слова", blank=True, null=True)
    sort = models.IntegerField(_("Сортировка"), default=0)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=True, null=True)

    class Meta:
        ordering = ['-sort', ]
        verbose_name = _("Текст")
        verbose_name_plural = _("Тексты")

    def __str__(self):
        return self.text
