from django.contrib import admin
from .models import Section, Article, ArticleMedia


class ArticleMediaAdmin(admin.StackedInline):
    model = ArticleMedia
    extra = 0
    classes = ['collapse']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleMediaAdmin]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
