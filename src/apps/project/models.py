from src.utils.base.models import Timestampble, Permalinkable
from django.db import models
from slugify import slugify
from src.apps.post_info.models import Like, Comment, View


def get_unique_string(name):
    base_slug = slugify(name)
    unique_slug = base_slug
    counter = 1
    while Project.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}_{counter}"
        counter += 1
    return unique_slug


class Project(Timestampble, Permalinkable):
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name='projects_created'
    )
    categories = models.ManyToManyField(
        'handbook.Category',
        verbose_name="Категории",
    )
    tags = models.ManyToManyField(
        'handbook.Tag',
        verbose_name="Теги",
        blank=True
    )
    members = models.ManyToManyField(
        'accounts.User',
        verbose_name="Участники",
        blank=True,
        related_name='projects_contributed'
    )
    images = models.ManyToManyField(
        'gallery.Image',
        verbose_name="Изображения",
        blank=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    likes_count = models.IntegerField(
        verbose_name="Количество лайков",
        default=0
    )
    comments_count = models.IntegerField(
        verbose_name="Количество комментарий",
        default=0
    )
    views_count = models.IntegerField(
        verbose_name="Количество просмотров",
        default=0
    )
    downloads_count = models.IntegerField(
        verbose_name="Количество скачиваний",
        default=0
    )
    file = models.FileField(
        upload_to='projects/uploads/',
        blank=True
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        try:
            project = Project.objects.get(pk=self.pk)
        except Project.DoesNotExist:
            project = False
        if project:
            if self.name != project.name:
                self.slug = get_unique_string(self.name)
        else:
            self.slug = get_unique_string(self.name)
        super().save(*args, **kwargs)
    
    def update_likes_count(self):
        self.likes_count = Like.objects.filter(project=self).count()
        self.save(update_fields=['likes_count'])

    def update_views_count(self):
        self.views_count = View.objects.filter(project=self).count()
        self.save(update_fields=['views_count'])

    def update_downloads_count(self):
        self.downloads_count = View.objects.filter(project=self).count()
        self.save(update_fields=['downloads_count'])

    def update_comments_count(self):
        self.comments_count = Comment.objects.filter(project=self).count()
        self.save(update_fields=['comments_count'])

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-id',)




class Application(Timestampble):
    project = models.ForeignKey(
        Project,
        verbose_name="Проект",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'accounts.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )


    def __str__(self):
        return f"{self.user.full_name} - {self.project.name}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-id',)
