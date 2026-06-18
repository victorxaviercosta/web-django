from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_timestamp")
    search_fields = ("title", "content")