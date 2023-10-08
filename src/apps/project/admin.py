from django.contrib import admin
from .models import (
    Project,
    Application
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Project.
    """
    list_display = (
        'name',
        'slug',
        'downloads_count',
        'likes_count',
        'comments_count',
        'views_count',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'categories',
    )
    autocomplete_fields = (
        'user',
        'categories',
        'tags',
        'members',
        'images',
    )
    readonly_fields = (
        'downloads_count',
        'likes_count',
        'comments_count',
        'views_count',
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }






@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Application.
    """
    list_display = (
        'project',
        'user',
        'description'
    )
    list_filter = (
        'project',
        'user',
    )
    autocomplete_fields = (
        'project',
        'user',
    )
