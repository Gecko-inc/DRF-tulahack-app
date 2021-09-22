import json
import os
from pprint import pprint

from django.core.management import BaseCommand

from django_template import settings
from section.models import Article, Section, ArticleMedia


class Command(BaseCommand):
    """
        Принимает json файл передаваемый как
        параметр в командной строке
    """
    help = "Импорт разделов/статей/картинок в базу данных"

    def add_arguments(self, parser):
        parser.add_argument("--file", nargs=1, default="chapter.json")

    def handle(self, *args, **options):
        data, to_create_sections, to_update_sections = [], [], []
        to_create_articles, to_update_articles = [], []
        to_create_media, to_update_media = [], []

        try:
            filename = os.path.join(settings.BASE_DIR, 'section', 'import', options['file'])
            with open(filename, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Файл не существует")
        except KeyError:
            print("Вы не передали параметр --file")
        except json.decoder.JSONDecodeError as e:
            print("У вас ошибка в json-е.\nOriginal Exception", e)

        data = [
            {
                "id": section['id'] + 1,
                "title": section['title'],
                "articles": [
                    {
                        "id": "",
                        # "number": article['number'],
                        "title": article['articleTitle'],
                        "section_id": section['id'] + 1,
                        "images": [
                            {
                                "id": "",
                                "text": image.get('text') or "",
                                "image": image.get('img') or "",
                                "article_id": article['key']
                            }
                            for image in article['contentText']
                        ]
                    }
                    for article in section['detail']
                ]
            }
            for section in data
        ]

        if data:
            articles_list = [section.pop('articles', None) for section in data]  # Список списков
            articles = [article for sub_article in articles_list for article in sub_article]  # Список словарей

            media_list = [article.pop('images', None) for article in articles]  # Список списков
            media = [item for sub_media in media_list for item in sub_media]  # Список словарей

            id_counter = 1

            for item in articles:
                item['id'] = id_counter
                id_counter += 1

            id_counter = 1
            for item in media:
                item['id'] = id_counter
                id_counter += 1

            sections = data

            existing_sections = Section.objects.all()
            existing_articles = Article.objects.all()
            existing_media = ArticleMedia.objects.all()

            existing_sections_titles = {item.title: item for item in existing_sections}
            existing_articles_titles = {item.title: item for item in existing_articles}
            existing_media_titles = {item.text: item for item in existing_media}

            for section in sections:
                if section['title'] in existing_sections_titles:
                    instance = existing_sections_titles[section['title']]
                    instance.title = section['title']
                    to_update_sections.append(instance)
                else:
                    to_create_sections.append(section)

            for article in articles:
                if article['title'] in existing_articles_titles:
                    instance = existing_articles_titles[article['title']]
                    # instance.number = article['number']
                    instance.title = article['title']
                    to_update_articles.append(instance)
                else:
                    to_create_articles.append(article)

            for item in media:
                if item['text'] in existing_media_titles:
                    instance = existing_media_titles[item['text']]
                    instance.text = item.get('text')
                    instance.image = item.get('image')
                    to_update_media.append(instance)
                else:
                    to_create_media.append(item)

            # Batch size for sqlite3 is 999, setting to 100 (found by practice)

            if to_update_sections:
                Section.objects.bulk_update(to_update_sections, ['title'], batch_size=100)

            if to_create_sections:
                sections = [Section(**section) for section in to_create_sections]
                Section.objects.bulk_create(sections, batch_size=100)

            if to_update_articles:
                Article.objects.bulk_update(to_update_articles, ['title'], batch_size=100)
            if to_create_articles:
                articles = [Article(**article) for article in to_create_articles]
                Article.objects.bulk_create(articles, batch_size=100)

            if to_update_media:
                ArticleMedia.objects.bulk_update(to_update_media, ['text', 'image'], batch_size=100)
            if to_create_media:
                media = [ArticleMedia(**media) for media in to_create_media]
                ArticleMedia.objects.bulk_create(media, batch_size=100)
