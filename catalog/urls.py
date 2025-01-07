from django.core.cache import cache

from django.urls import path
from . import views
from django.contrib import admin
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductDeleteView, ProductUpdateView,ProductListView, ProductDetailView
from .models import Product
from django.conf import settings
from django.conf.urls.static import static
# app_name = 'catalog'
app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>',cache_page(60)(ProductDetailView.as_view(), name='product_detail')),
    path('catalog/new/',ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/edit/',ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),
]



