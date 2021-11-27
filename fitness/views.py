from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config.views import init_user
from fitness.models import UserFitness
from fitness.serializers import UserFitnessSerializer


class GetUserFitness(RetrieveUpdateDestroyAPIView):
    model = UserFitness
    queryset = UserFitness.objects.all()
    serializer_class = UserFitnessSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["UserFitness"])
    def get(self, request, *args, **kwargs):
        if request.data:
            user_fitness = self.queryset.filter(user_id=init_user(request))
            serializer = self.serializer_class(user_fitness, many=True)
            return Response(serializer.data, status=200)
        return Response({"response": "no data provided"}, status=500)

    @swagger_auto_schema(tags=["UserFitness"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=["user_id"],
                             properties={
                                 "created": openapi.Schema(type=openapi.FORMAT_DATETIME),
                                 "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "unit": openapi.Schema(type=openapi.TYPE_STRING),
                                 "exercise_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "progress": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "is_current": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                             }))
    def post(self, request, *args, **kwargs):
        if request.data:
            try:
                user_fitness = self.model.objects.bulk_create(
                    [self.model(user_id=init_user(request).id, **request.data)])
                serializer = self.serializer_class(user_fitness, many=True)
            except Exception as e:
                print(e)
                return Response({}, status=400)
            return Response(serializer.data, status=200)
        return Response({"response": "no data provided"}, status=500)

    @swagger_auto_schema(tags=["UserFitness"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=["id", "user_id"],
                             properties={
                                 "created": openapi.Schema(type=openapi.FORMAT_DATETIME),
                                 "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "unit": openapi.Schema(type=openapi.TYPE_STRING),
                                 "exercise_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "progress": openapi.Schema(type=openapi.TYPE_INTEGER),
                                 "is_current": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                             }))
    def put(self, request, *args, **kwargs):
        data = dict(request.data.copy())
        if data:
            instance = self.model.objects.get(id=data.get('id'))
            for attr, val in data.items():
                setattr(instance, attr, val)
            try:
                data.pop('id')  # Удаление из словаря id, для bulk_update
                self.model.objects.bulk_update([instance], data.keys())
            except Exception as e:
                print(e)
                return Response(status=500)
            return Response(status=200)
        return Response({"response": "no data provided"}, status=500)

    @swagger_auto_schema(tags=["UserFitness"],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=["id"],
                             properties={
                                 "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                             }))
    def delete(self, request, *args, **kwargs):
        if request.data:
            self.model.objects.get(id=request.data.get('id', None)).delete()
            return Response({"response": f"{request.data.get('id', None)} deleted"})
        return Response({"response": "no data provided"}, status=500)
