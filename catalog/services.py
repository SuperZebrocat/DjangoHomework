from catalog.models import Product
from django.core.cache import cache

from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


def get_products_from_cache(user):
    if not CACHE_ENABLED:
        if user.is_authenticated:
            return Product.objects.all()
        else:
            return Product.objects.filter(is_published=True)

    cache_key = f'product_list_{user.id}' if user.is_authenticated else 'product_list_published'
    products = cache.get(cache_key)

    if products is not None:
        return products

    if user.is_authenticated:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(is_published=True)

    cache.set(cache_key, products)
    return products
