from django.contrib import admin

from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published', 'views_counter')
    list_filter = ('title',)
    search_fields = ('title', 'content',)

