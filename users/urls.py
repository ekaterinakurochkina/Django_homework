from tempfile import template

from django.urls import path
from . import views
from django.contrib import admin
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView

# from catalog.views import ProductCreateView, ProductDeleteView, ProductUpdateView,ProductListView, ProductDetailView
from .models import User
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'user'
app_name = UsersConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

