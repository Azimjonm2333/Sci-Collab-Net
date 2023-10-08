from django.utils.html import format_html


class AvatarMixin:
    def show_avatar(self, obj):
        return format_html(f'<img src="{obj.avatar_url}" width="50" height="50" />')

    show_avatar.short_description = 'Аватар'
