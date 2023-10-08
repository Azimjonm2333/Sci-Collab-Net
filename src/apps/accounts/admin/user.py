from django.contrib import admin
from ..mixins import AvatarMixin
from ..models import UserProfile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(AvatarMixin, admin.StackedInline):
    """
    Inline для профиля клиента.

    Позволяет редактировать профиль клиента внутри административной панели.
    """
    model = UserProfile
    verbose_name = "Профиль"
    min_num = 1
    readonly_fields = ('show_avatar',)
    fields = (
        ("show_avatar", "avatar",),
        ("first_name", 'last_name',),
        ("description",),
        ("categories",)
    )
    autocomplete_fields = (
        "categories",
    )


@admin.register(User)
class UserAdmin(AvatarMixin, BaseUserAdmin):
    """
    Административная панель для модели Client.

    Здесь можно настроить отображение и редактирование клиентов.
    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'phone',
                'email',
                'password1',
                'password2',
            ),
        }),
    )
    fieldsets = ()
    list_display = (
        'username',
        'show_avatar',
        'phone',
        'is_staff',
        'is_verify',
    )
    search_fields = ('username', 'phone',)
    ordering = ('username', 'phone',)
    inlines = [UserProfileInline]

    def get_full_name(self, obj):
        return obj.full_name

    get_full_name.short_description = 'Имя и фамилия'



