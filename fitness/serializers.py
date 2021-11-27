from rest_framework import serializers

from fitness.models import *


class UserFitnessSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%YT%H:%m")

    class Meta:
        model = UserFitness
        exclude = ["sort", ]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
