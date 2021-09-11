from rest_framework import serializers
from .models import Section, Article, ArticleMedia


class ArticleMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = [
            'text',
            'image',
        ]


class ArticleSerializer(serializers.ModelSerializer):
    detail = ArticleMediaSerializer(many=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'detail',
        ]


class SectionSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Section
        fields = [
            "id",
            "title",
            "articles",
        ]
