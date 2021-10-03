from django.contrib import admin
from .models import Section, Article, ArticleMedia


class ArticleMediaAdmin(admin.StackedInline):
    model = ArticleMedia
    extra = 0
    classes = ['collapse']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleMediaAdmin]
    list_display = ['id', 'title', 'media_count']

    def media_count(self, obj):
        return len(obj.detail.all())

    media_count.short_description = "Вложений"


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
