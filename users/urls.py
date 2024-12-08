from tempfile import template

from django.urls import path
from . import views
from django.contrib import admin
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import logout_view
from django.core.mail import send_mail

# from catalog.views import ProductCreateView, ProductDeleteView, ProductUpdateView,ProductListView, ProductDetailView
from .models import User
from django.conf import settings
from django.conf.urls.static import static

from .views import UserCreateView

# app_name = 'user'
app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('send_mail',send_mail, name='send_mail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

