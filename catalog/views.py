from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    print(context)
    return render(request, "home.html", context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        return HttpResponse(f'Спасибо {name}, мы свяжемся с вами по номеру {phone}')
    return render(request, "contacts.html")


def products_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, "products_detail.html", context=context)