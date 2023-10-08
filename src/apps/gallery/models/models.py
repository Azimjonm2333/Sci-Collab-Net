import os
from urllib.request import urlopen
from django.core.exceptions import ValidationError
from django.core.files import File
from django.db import models
from src.apps.gallery.utils import validate_image_url, create_thumbnail
from src.utils.base.models import Timestampble


class Folder(Timestampble):
    name: str = models.CharField('Папка', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Папка"
        verbose_name_plural = "Папки"


class Image(Timestampble):
    original = models.ImageField(
        verbose_name="Оригинал",
        blank=True,
        null=True,
        upload_to="images/original/",
    )
    original_url = models.URLField(
        verbose_name="URL",
        blank=True,
        null=True,
        validators=[validate_image_url],
        max_length=1000,
    )
    thumbnail = models.ImageField(
        verbose_name="Миниатюрка",
        upload_to="images/thumbnail/",
        blank=True,
        null=True,
    )
    folder = models.ForeignKey(
        Folder,
        verbose_name="Папка",
        on_delete=models.CASCADE
    )

    @property
    def get_original_url(self):
        if self.original:
            return self.original.url
        return self.original_url

    @property
    def get_thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url

    def clean(self):
        if not self.original and not self.original_url:
            raise ValidationError("Either 'original' or 'original_url' must be provided.")

    def save(self, *args, **kwargs):
        if self.original_url and not self.original:
            response = urlopen(self.original_url)
            image_name = os.path.basename(self.original_url)
            self.original.save(image_name, File(response))
            super().save(*args, **kwargs)

        if self.original:
            self.thumbnail = create_thumbnail(self.original)

    def delete(self, *args, **kwargs):
        if self.original:
            storage, path = self.original.storage, self.original.path
            storage.delete(path)
        if self.thumbnail:
            storage, path = self.thumbnail.storage, self.thumbnail.path
            storage.delete(path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
