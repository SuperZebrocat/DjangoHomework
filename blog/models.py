from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    article = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['is_published']

    def __str__(self):
        return self.title
