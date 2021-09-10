from django.contrib import admin
from .models import Config


@admin.register(Config)
class CfgAdmin(admin.ModelAdmin):
    list_display = ['title', 'key', 'value']
    list_editable = ['value']
