from django.shortcuts import render
from .checkout import Checkout

# Create your views here.


def checkout_summary(request):
    return render(request, 'checkout/checkout-summary.html')


def checkout_add(request):
    
    checkout = Checkout(request)
    if request.POST.get('action') == 'post':
         product_id = int(request.POST.get('product_id'))
         product_quantity = int(request.POST.get('product_quantity'))


def checkout_delete(request):
    pass


def checkout_update(request):
    pass

