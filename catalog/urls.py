from django.urls import path
from . import views
from django.contrib import admin
from catalog.apps import CatalogConfig


# app_name = 'catalog'
app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('contacts/', views.contact_data, name='contact_data'),
    path('base/', views.base, name='base'),
    path('products_list/', views.products_list, name='products_list'),
    path('product_detail/', views.product_detail, name='product_detail'),
]

