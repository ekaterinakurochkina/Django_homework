from django.urls import path
from . import views
from django.contrib import admin
from catalog.apps import CatalogConfig
# from catalog.views import products_list, product_detail, ProductListView
from catalog.views import ProductListView, ProductDetailView
from .models import Product
from django.conf import settings
from django.conf.urls.static import static
# app_name = 'catalog'
app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home, name='home'),
    # path('contacts/', views.contact_data, name='contact_data'),
    path('base/', views.base, name='base'),
    # path('products_list/', views.products_list, name='products_list'),
    path('', ProductListView.as_view(), name='products_list'),
    # path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('product/<int:pk>',ProductDetailView.as_view(), name='product_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

