from django.urls import path
from . import views
from django.contrib import admin


app_name = 'catalog'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('contacts/', views.contact_data, name='contact_data'),
    path('base/', views.base, name='base'),
]

