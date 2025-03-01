from .models import Product
from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем текущего пользователя как владельца
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_edit.html'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if not (request.user.groups.filter(name='product moderator').exists() or product.owner == request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if not (request.user.groups.filter(name='product moderator').exists() or product.owner == request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Product.objects.all()
        else:
            return Product.objects.filter(is_published=True)


@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
