from django.shortcuts import get_object_or_404, render

from .models import Banner, Category, Product


def home(request):
    products = Product.objects.all()
    banners = Banner.banners.all()
    return render(request, 'store/home.html', {'products': products, 'banners': banners})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

  