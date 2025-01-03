from django.urls import path
from .views import BlogsListView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView, BlogsDetailView
from blogs.models import Blogs

app_name = 'blogs'
# app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs_list'),
    path('blogs/<int:pk>/', BlogsDetailView.as_view(), name='blogs_detail'),
    path('blogs/new/', BlogsCreateView.as_view(), name='blogs_create'),
    path('blogs/<int:pk>/edit/', BlogsUpdateView.as_view(), name='blogs_edit'),
    path('blogs/<int:pk>/delete/', BlogsDeleteView.as_view(), name='blogs_delete'),
]