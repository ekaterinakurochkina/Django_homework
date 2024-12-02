# coding: utf-8
from catalog.models import Product, Category
categories = Category.objects.all()
for category in categories:
    print(f"ID:{category.id},Название:{category.name}")
    
products = Product.objects.all()
for product in products:
    print(f"Продукт:{product.name} из категории:{product.category}")
    
