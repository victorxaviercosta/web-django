from django.contrib import admin

from .models import Message, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "creation_timestamp")
    search_fields = ("title", "content")