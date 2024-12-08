from tempfile import template

from django.urls import path
from . import views
from django.contrib import admin
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView

# from catalog.views import ProductCreateView, ProductDeleteView, ProductUpdateView,ProductListView, ProductDetailView
from .models import User
from django.conf import settings
from django.conf.urls.static import static

from .views import UserCreateView

# app_name = 'user'
app_name = UsersConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

