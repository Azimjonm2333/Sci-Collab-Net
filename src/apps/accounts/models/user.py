from django.db import models
from django.contrib.auth.models import AbstractUser
from src.utils.base.models import Timestampble
from ..managers import UserManager
from src.apps.handbook.models import Category


class User(AbstractUser, Timestampble):
    first_name = None
    last_name = None

    email = models.EmailField(
        verbose_name="Email",
        blank=False,
        unique=True,
        max_length=200
    )
    phone = models.CharField(
        verbose_name='Телефон',
        blank=True,
        max_length=15
    )
    otp = models.IntegerField(default=0)
    is_verify = models.BooleanField(default=False)

    objects = UserManager()


    @property
    def profile(self):
        return self.userprofile

    @property
    def full_name(self):
        return f"{self.profile.first_name} {self.profile.last_name}"

    @property
    def avatar_url(self):
        return self.profile.avatar_url

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        # proxy = True



class UserProfile(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=150, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="avatars/clients/",
        blank=True,
        null=True,
        verbose_name="Аватар"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name="Категории",
        blank=True,
    )

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return "/static/accounts/default_avatar.jpg"

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
