from django.contrib import admin

from .models import MobileUser, Bookmark


class BookmarkAdmin(admin.StackedInline):
    model = Bookmark
    extra = 0
    classes = ['collapse']


@admin.register(MobileUser)
class MobileUserAdmin(admin.ModelAdmin):
    readonly_fields = ["date_joined"]
    inlines = [BookmarkAdmin]
