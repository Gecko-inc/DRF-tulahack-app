import random

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView

from config.views import generate_token, get_qiwi_url, check_qiwi_pay

from django.utils.translation import gettext_lazy as _

#
# class BookmarkDeleteView(APIView):
#     @swagger_auto_schema(
#         tags=['Bookmark'],
#         manual_parameters=[
#             openapi.Parameter('mark_id', openapi.IN_PATH, description=_('Идентификатор закладки.'),
#                               required=True,
#                               type=openapi.TYPE_INTEGER)
#         ]
#     )
#     def delete(self, request, **kwargs):
#         try:
#             Bookmark.objects.get(id=kwargs.get("mark_id")).delete()
#         except Bookmark.DoesNotExist:
#             pass
#         return Response(status=200)
#
#
# class BookmarkListView(ListAPIView):
#     """
#       Получение закладок пользователя
#     """
#
#     @swagger_auto_schema(tags=['Bookmark'], manual_parameters=[
#         openapi.Parameter('token', openapi.IN_QUERY, description=_('Токен'),
#                           required=True, type=openapi.TYPE_STRING),
#     ],
#                          )
#     def get(self, request):
#         return Response(BookmarkSerializer(
#             Bookmark.objects.filter(user__token=request.GET.get("token")), many=True).data)
#
#
# class UserView(APIView):
#     """
#       Получение информации о пользователе
#     """
#
#     @swagger_auto_schema(tags=['User'], manual_parameters=[
#         openapi.Parameter('token', openapi.IN_QUERY, description=_('Токен'),
#                           required=True, type=openapi.TYPE_STRING),
#     ],
#                          )
#     def get(self, request):
#         try:
#             queryset = MobileUser.objects.get(token=request.GET.get("token"))
#             return Response(MobileUserSerializer(queryset, many=False).data)
#         except MobileUser.DoesNotExist:
#             return Response(status=404)

#
# class BookmarkAPIView(APIView):
#
#     @swagger_auto_schema(tags=['Bookmark'],
#                          request_body=openapi.Schema(
#                              type=openapi.TYPE_OBJECT,
#                              required=['token', "article_id"],
#                              properties={
#                                  'token': openapi.Schema(type=openapi.TYPE_STRING),
#                                  'article_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                              },
#                          ),
#                          )
#     def post(self, request, *args, **kwargs):
#         """
#           Создание закладки
#         """
#         data = request.data
#         try:
#             Bookmark.objects.create(
#                 user=MobileUser.objects.get(token=data.get("token")),
#                 article=Article.objects.get(id=data.get("article_id"))
#             )
#         except MobileUser.DoesNotExist:
#             return Response(status=404)
#         except Article.DoesNotExist:
#             return Response(status=404)
#         return Response(status=201)
#
#
# class UserAPIView(APIView):
#
#     @swagger_auto_schema(tags=['User'])
#     def post(self, request, *args, **kwargs):
#         """
#           Создание пользователя по уникальному ключу
#         """
#         headers = request.headers
#         unique_arg = f"""
#         {headers.get('Host')}{headers.get('Origin')}{headers.get('Sec-Ch-Ua-Platform')}{random.randint(0, 21)}
#         """
#         token = generate_token(unique_arg=unique_arg)
#         MobileUser.objects.create(
#             token=token
#         )
#         return Response({
#             "token": token
#         })
#
#
# class PayUrl(APIView):
#
#     @swagger_auto_schema(tags=['Pay'], manual_parameters=[
#         openapi.Parameter('token', openapi.IN_QUERY, description=_('Токен пользователя.'),
#                           required=True,
#                           type=openapi.TYPE_STRING)
#
#     ])
#     def get(self, request):
#         return Response({
#             "url": get_qiwi_url(request.GET.get("token"))
#         })
#
#
# class CheckPay(APIView):
#
#     @swagger_auto_schema(tags=['Pay'], manual_parameters=[
#         openapi.Parameter('token', openapi.IN_QUERY, description=_('Токен пользователя.'),
#                           required=True,
#                           type=openapi.TYPE_STRING)
#
#     ])
#     def get(self, request):
#         try:
#             user = MobileUser.objects.get(token=request.GET.get("token"))
#             if check_qiwi_pay(request.GET.get("token")):
#                 user.is_premium = check_qiwi_pay(request.GET.get("token"))
#                 user.save()
#             return Response({
#                 "pay": check_qiwi_pay(request.GET.get("token"))
#             })
#         except MobileUser.DoesNotExist:
#             return Response({
#                 "status": 404,
#                 "error": "User does not exist"
#             })
