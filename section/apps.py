from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'section'
    verbose_name = _("Книга")
