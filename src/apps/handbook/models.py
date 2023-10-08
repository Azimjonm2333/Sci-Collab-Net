from src.utils.base.models import Timestampble, Permalinkable
from django.db import models
from slugify import slugify
from src.apps.gallery.models import Image


class Tag(Timestampble, Permalinkable):
    """ Tag """
    name: str = models.CharField(verbose_name="Названия", max_length=200, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ('-id',)


class Category(Timestampble, Permalinkable):
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родитель",
        related_name='category_children',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def children(self):
        return list(self.category_children.all())

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)


