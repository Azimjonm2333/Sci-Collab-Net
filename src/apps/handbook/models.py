from src.utils.base.models import Timestampble, Permalinkable
from django.db import models
from slugify import slugify


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


class Chat(Timestampble):

    participants = models.ManyToManyField('accounts.User', related_name='chats')

    def __str__(self):
        return ', '.join([str(participant) for participant in self.participants.all()])

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ('created_at',)




class Message(Timestampble):
    chat = models.ForeignKey(
        Chat,
        verbose_name="Чат",
        related_name='messages',
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        'accounts.User',
        verbose_name="Отправитель",
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )

    def __str__(self):
        return f"{self.sender.username} - {self.message}"


    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщении'
        ordering = ('created_at',)




class Favorites(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        'project.Project',
        verbose_name="Проект",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ['-id']

    def __str__(self) -> str:
        return f"{self.user.username} - {self.project.name}"

