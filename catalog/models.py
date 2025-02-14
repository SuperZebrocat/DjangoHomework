from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    description = models.CharField(max_length=100, verbose_name='Описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение продукта', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(verbose_name='Цена продукта', null=True)
    is_published = models.BooleanField(default=False, verbose_name='Добавить продукт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

    def __str__(self):
        return self.name
