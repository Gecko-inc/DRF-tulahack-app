from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from todo.serializer import *


class TodoView(RetrieveUpdateDestroyAPIView):
    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @swagger_auto_schema(tags=["Todo"])
    def get(self, request, *args, **kwargs):
        if request.data:
            serializer = self.serializer_class(self.model.objects.all(), many=True)
            return Response(serializer.data, status=200)
        return Response(status=500)

    @swagger_auto_schema(tags=["Todo"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "title": openapi.Schema(type=openapi.TYPE_STRING),
                                 "created": openapi.Schema(type=openapi.FORMAT_DATETIME),
                             }
                         ))
    def post(self, request, *args, **kwargs):
        data = dict(request.data.copy())
        if data:
            todo = self.model.objects.bulk_create([self.model(**data)])
            serializer = self.serializer_class(todo)
            return Response(serializer.data, status=200)
        return Response(status=500)

    @swagger_auto_schema(tags=["Todo"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['id'],
                             properties={
                                 "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "title": openapi.Schema(type=openapi.TYPE_STRING),
                                 "created": openapi.Schema(type=openapi.FORMAT_DATETIME)
                             }
                         ))
    def put(self, request, *args, **kwargs):
        data = dict(request.data.copy())
        if data:
            todo = self.model.objects.get(id=data.get('id'))
            for attr, val in data.items():
                setattr(todo, attr, val)
            self.model.objects.bulk_update([todo], data.keys())
            serializer = self.serializer_class(todo)
            return Response(serializer.data, status=200)
        return Response(status=500)

    @swagger_auto_schema(tags=["Todo"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['id'],
                             properties={
                                 "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                             }
                         ))
    def delete(self, request, *args, **kwargs):
        if request.data:
            self.model.objects.get(id=request.data.get('id')).delete()
            return Response(status=200)
        return Response(status=500)
