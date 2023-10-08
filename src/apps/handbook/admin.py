from django.contrib import admin
from .models import (
    Tag,
    Category,
)
from django.utils.safestring import mark_safe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Tag.
    """
    search_fields = (
        'name',
    )
    list_display = (
        'name',
        'slug',
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Category.
    """
    list_display = (
        'name',
        'slug',
        'parent'
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'parent',
    )
    autocomplete_fields = (
        "parent",
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
