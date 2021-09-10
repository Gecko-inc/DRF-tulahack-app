from django.contrib import admin
from .models import Section, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
