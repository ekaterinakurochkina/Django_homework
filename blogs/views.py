from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogs.models import Blogs
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView, DetailView
from django.urls import reverse_lazy


class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs/blogs_detail.html'
    context_object_name = 'blog'


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs/blogs_form.html'
    success_url = reverse_lazy('blogs_list')


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs/blogs_form.html'
    success_url = reverse_lazy('blogs_list')


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = 'blogs/blogs_confirm_delete.html'
    success_url = reverse_lazy('blogs_list')