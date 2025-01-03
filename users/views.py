import secrets
from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy, reverse
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.contrib.auth import logout, login
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def logout_view(request):
    logout(request)
    return redirect('catalog:product_list')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)  # генерируем токен
        user.token = token
        user.save()
        host = self.request.get_host()   # получаем хост, откуда пришел пользователь
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Добро пожаловать в наш сервис",
            message=f"""Спасибо, что зарегистрировались в нашем сервисе! 
            Для подтверждения регистрации перейдите по ссылке {url}""",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy("users:login"))
