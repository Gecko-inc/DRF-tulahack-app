from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import UserStatus, User


@admin.register(User)
class PersonAdmin(UserAdmin):
    actions = None
    list_display = ('id', 'username', 'is_active')
    list_filter = ('status', 'is_active',)
    list_display_links = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_("Основная информация"), {'fields': ('email', 'status')}),
        (_("Статус"), {'fields': ('is_active', 'is_staff', 'is_superuser',), }),
        (_("Дополнительная информация"), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    pass
