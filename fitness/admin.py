from django.contrib import admin

from fitness.models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)


@admin.register(UserFitness)
class UserFitnessAdmin(admin.ModelAdmin):
    list_display = ("user", "exercise", "is_current",)
    list_editable = ['is_current', ]
