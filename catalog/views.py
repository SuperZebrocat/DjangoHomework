from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
