from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache


def get_product_from_cache():
    """Функция низкоуровневого кеширования для списка продуктов"""
    if not CACHE_ENABLED:
        return Product.objects.all() # проверяем, используется ли кеширование в проекте
    key = "product_list"        # задаем ключ
    products = cache.get(key)   # обращаемся в кеш по этому ключу
    if products is not None:
        return products         # если кеш пуст
    products = Product.objects.all()    # забираем список продуктов из БД
    cache.set(key, products)    # записываем этот список в кеш
    return products             # и выдаем пользователю


def get_product_category(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category=Category.objects.get(pk=category_id))
    key = f'product_list_from_category_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    cache.set(key, products, 60)
    return products

#     category = Category.object.name
#     products = Product.filter("category_id")
#     if products is None:
#         return "В этой категории нет ни одного товара"
#     else:
#         return Product.object.filter("category")
