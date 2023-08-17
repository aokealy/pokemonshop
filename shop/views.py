from django.shortcuts import render
from . models import Category, Product


# Create your views here.

def shop(request):
    all_products = Product.objects.all()

    context = {'shop_products': all_products}

    return render(request, 'shop/shop.html', context)


def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


