from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import DeleteView, CreateView, UpdateView, ListView, DetailView
from .forms import ProductForm
from .models import Product

class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_list.html'
    success_url = 'catalog/product_list'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = 'catalog/product_list'

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_detail.html'
    success_url = 'catalog/product_list'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_detail.html'
    success_url = 'catalog/product_list'

class ProductDetailView(DetailView):
    model = Product
#
#
# def home(request):
#     return render(request, 'catalog/home.html')
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')
#
# def base(request):
#     return render(request, 'catalog/base.html')

# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request,'catalog/products_list.html', context)

# def product_detail(request, pk):
#     # product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context)

# def contact_data(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'catalog/contacts.html')