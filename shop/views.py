from django.shortcuts import render
from . models import Category

# Create your views here.

def shop(request):

    return render(request, 'shop/shop.html')


def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


