# import cgi
#
# from bs4 import BeautifulSoup
# import lxml
# from django.http import JsonResponse
# from rest_framework.generics import RetrieveAPIView
# from rest_framework.response import Response
#
# from section.models import Section, ArticleMedia
# from section.serializer import SectionSerializer
#
#
# def format_rich_text(rich_text):
#     if rich_text:
#         soup = BeautifulSoup(rich_text, 'lxml')
#         ps = soup.find_all('p')
#         for p in ps:
#             p.name = "Text"
#         spans = soup.find_all('span')
#         for span in spans:
#             span.name = "Text"
#         for tag in soup():
#             del tag['style']
#
#         return str(soup)
#
#
# class SectionRichFormatView(RetrieveAPIView):
#     queryset = Section.objects.all()
#     serializer_class = SectionSerializer
#
#     def get(self, request, *args, **kwargs):
#         section = self.get_queryset()
#         articles = section.articles.all()
#         article_media = ArticleMedia.objects.all()
#         article_ids = {item.id: item for item in articles}
#
#         # Для уменьшения запросов в бд
#         article_media_items = []
#         for media in article_media:
#             if media.article_id in article_ids:
#                 article_media_items.append(media)
#
#         data = [
#             {
#                 "id": section.id,
#                 "title": section.title,
#                 "articles": [
#                     {
#                         "id": article.id,
#                         "title": article.title,
#                         "detail": [
#                             {
#                                 "text": media.text,
#                                 "rich_text": format_rich_text(media.rich_text),
#                                 "word": media.word,
#                                 "additional_text": media.additional_text,
#                                 "image": media.image.name
#                             }
#                             for media in article_media_items
#                         ]
#                     }
#                     for article in articles
#                 ]
#             }
#         ]
#         return JsonResponse(data, safe=False)
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk', None)
#         if not pk:
#             return self.queryset.all()
#         return self.queryset.get(id=3)
