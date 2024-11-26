from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(max_length=500, verbose_name='Содержимое', blank=True)
    image = models.ImageField(upload_to='blogs/images/', verbose_name='Изображение', help_text='Загрузите изображение', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров",help_text="Укажите количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title']
