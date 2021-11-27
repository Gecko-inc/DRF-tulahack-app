from rest_framework import serializers

from fitness.models import *


class UserFitnessSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%YT%H:%m")

    class Meta:
        model = UserFitness
        fields = "__all__"
