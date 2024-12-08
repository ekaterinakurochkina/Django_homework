from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail


def logout_view(request):
    logout(request)
    return redirect('catalog:product_list')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def send_mail(self,form):
        user = form.save
        send_mail(
            subject = "Подтверждение регистрации",
            message = "Благодарим за регистрацию на сайте!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().send_mail(form)




