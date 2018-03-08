from django.contrib import admin

from django.contrib import admin
from . import models as app_models


@admin.register(app_models.Counter)
class TaskFlowAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', 'msg']
    ordering = ['id']
    readonly_fields = ['count']

