from django.contrib import admin

from step.models import Step


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "count")