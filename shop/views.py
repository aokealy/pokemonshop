from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


# Create your views here.


def shop(request):
    """Display all Products on Page"""
    all_products = Product.objects.all()

    context = {"shop_products": all_products}

    return render(request, "shop/shop.html", context)


def categories(request):
    """Display all Categories on Page"""
    all_categories = Category.objects.all()

    return {"all_categories": all_categories}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(
        request,
        "shop/list-category.html",
        {"category": category, "products": products},
    )


def product_information(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {"product": product}

    return render(request, "shop/product-information.html", context)
