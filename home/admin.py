from django.contrib import admin

from .models import Message, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "creation_timestamp")
    list_filter = ("category", "tags")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)