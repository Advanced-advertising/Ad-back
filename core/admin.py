from django.contrib import admin
from core.models import Screen


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'resolution', 'diagonal']
