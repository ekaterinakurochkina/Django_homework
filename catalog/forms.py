from xmlrpc.client import Boolean
from django.db import models


from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    # name = models.CharField(max_length=150, verbose_name='Наименование')
    # description = models.TextField(max_length=150, verbose_name='Описание', blank=True)
    # image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    # price = models.IntegerField(verbose_name='Цена за покупку', null=True)
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', null=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']
        exclude = ['created_at', 'updated_at']
#
# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if isinstance(field, BooleanField):
#                 field.widget.attrs['class']="form-check-input"
#             else:
#                 field.widget.attrs['class'] = "form-class"