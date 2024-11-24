from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogs.models import Blogs
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs_list.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs_detail.html'
    context_object_name = 'blog'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class BlogsCreateView(CreateView):
    model = Blogs
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs_form.html'
    success_url = reverse_lazy('blogs:blogs_list')


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs_form.html'
    success_url = reverse_lazy('blogs:blogs_list')


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = 'blogs_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs_list')