from django.contrib import admin
from .models import (
    Tag,
    Category,
    Favorites,
    Chat
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


@admin.register(Favorites)
class FavoriteAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Favorites.

    Здесь можно настроить отображение и фильтрацию списка избранных элементов.
    """
    list_display = (
        'user',
        'project'
    )
    autocomplete_fields = (
        "user",
        "project",
    )

    list_filter = (
        'user',
        'project',
    )
    search_fields = (
        'user__username',
        'project__name',
    )

    def project_description(self, obj):
        return obj.project.description

    project_description.short_description = 'Описание продукта'
    project_description.allow_tags = True





@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Chat.
    """
    list_display = (
        'from_user',
        'to_user',
        'message'
    )
    search_fields = (
        'from_user',
        'to_user',
    )
    list_filter = (
        'from_user',
        'to_user',
    )
    autocomplete_fields = (
        'from_user',
        'to_user',
    )
