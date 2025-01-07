from config.settings import CACHE_ENABLED
from catalog.models import Product
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
