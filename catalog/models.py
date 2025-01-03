from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=450, verbose_name='Описание', help_text="Введите описание продукта", blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price = models.IntegerField(verbose_name='Цена за покупку', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', null=True)
    is_published = models.BooleanField(verbose_name="Публикация продукта", default=False)
    # owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца товара", blank=True, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца товара", blank=True, default=User.email, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Can unpublish product")
        ]
