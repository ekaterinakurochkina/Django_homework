from tempfile import template

from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView
from users.views import logout_view, UserCreateView, email_verification
from users.views import logout_view
from django.conf import settings
from django.conf.urls.static import static

from .views import UserCreateView

# app_name = 'user'
app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>',email_verification, name='email-confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

