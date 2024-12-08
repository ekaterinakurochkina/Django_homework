from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
