from src.utils.base.models import Timestampble
from django.db import models



class Like(Timestampble):
    project = models.ForeignKey(
        'project.Project',
        verbose_name="Проект",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.full_name} - {self.project.name}"

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'



class View(Timestampble):
    project = models.ForeignKey(
        'project.Project',
        verbose_name="Проект",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.full_name} - {self.project.name}"

    class Meta:
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'





class Download(Timestampble):
    project = models.ForeignKey(
        'project.Project',
        verbose_name="Проект",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.full_name} - {self.project.name}"

    class Meta:
        verbose_name = 'Загрузка'
        verbose_name_plural = 'Загрузки'



class Comment(Timestampble):
    
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        'project.Project',
        verbose_name="Проект",
        on_delete=models.CASCADE,
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родитель",
        related_name='category_children',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.username} - {self.message}"

    @property
    def children(self):
        return list(self.category_children.all())

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


