from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Folder, Image


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Folder.

    Здесь можно настроить отображение и поиск папок.
    """
    search_fields = ("name",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Image.

    Здесь можно настроить отображение, фильтрацию и редактирование изображений.
    """
    search_fields = ("original_url",)
    autocomplete_fields = ("folder",)
    list_display = (
        'preview_thumbnail_image',
        'created_at',
        'folder',
    )

    list_filter = (
        'created_at',
        "folder"
    )
    readonly_fields = (
        'preview_original_image',
        'preview_thumbnail_image',
        'created_at',
        'updated_at',
    )
    fields = (
        'preview_original_image',
        'preview_thumbnail_image',
        'original',
        'original_url',
        'folder',
        'created_at',
        'updated_at'
    )

    def preview_thumbnail_image(self, obj):
        if obj.thumbnail:
            return mark_safe(f"<img src={obj.thumbnail.url} width={65} height={65} />")

    def preview_original_image(self, obj):
        if obj.original:
            return mark_safe(f"<img src={obj.original.url} width={300} height={300} />")

    preview_thumbnail_image.short_description = "Миниатюра"
    preview_original_image.short_description = "Оригинал"
