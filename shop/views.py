from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404


# Create your views here.

def shop(request):
    all_products = Product.objects.all()

    context = {'shop_products': all_products}

    return render(request, 'shop/shop.html', context)


def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def list_category(request):
    pass

   
def product_information(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}

    return render(request, 'shop/product-information.html', context)
