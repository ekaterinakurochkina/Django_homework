from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')

def base(request):
    return render(request, 'catalog/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request,'catalog/products_list.html', context)


def contact_data(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')