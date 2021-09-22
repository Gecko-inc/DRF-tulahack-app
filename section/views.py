from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from .models import Section
from .serializer import SectionSerializer


class SectionListView(ListAPIView):
    """
      Получение списка всех разделов
    """
    queryset = Section
    serializer_class = SectionSerializer

    @swagger_auto_schema(
        tags=['Section']
    )
    def get(self, request, **kwargs):
        queryset = self.queryset.objects.filter(is_active=True)
        return Response(self.serializer_class(queryset, many=True).data)


class SectionDetailView(APIView):
    """
      Получение раздела по ID
    """

    @swagger_auto_schema(
        tags=['Section'],
        manual_parameters=[
            openapi.Parameter('section_id', openapi.IN_PATH, description=_('Идентификатор раздела.'),
                              required=True,
                              type=openapi.TYPE_INTEGER)
        ]
    )
    def get(self, request, **kwargs):
        try:
            queryset = Section.objects.get(is_active=True, id=kwargs.get("section_id"))
            return Response(SectionSerializer(queryset, many=False).data)
        except Section.DoesNotExist:
            return Response(status=404)
