from django.contrib import admin
from .models import Like, Comment, View, Download



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Like.
    """
    list_display = (
        'project',
        'user',
    )
    list_filter = (
        'project',
        'user',
    )
    autocomplete_fields = (
        'project',
        'user',
    )



@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    """
    Административная панель для модели View.
    """
    list_display = (
        'project',
        'user',
    )
    list_filter = (
        'project',
        'user',
    )
    autocomplete_fields = (
        'project',
        'user',
    )




@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Download.
    """
    list_display = (
        'project',
        'user',
    )
    list_filter = (
        'project',
        'user',
    )
    autocomplete_fields = (
        'project',
        'user',
    )



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Comment.
    """
    list_display = (
        'user',
        'project',
        'message',
        'parent'
    )
    search_fields = (
        'message',
    )
    list_filter = (
        'user',
    )
    autocomplete_fields = (
        "user",
        'project',
        'parent'
    )

