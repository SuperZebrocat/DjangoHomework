from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        return HttpResponse(f'Спасибо {name}, мы свяжемся с вами по номеру {phone}')
    return render(request, "contacts.html")
