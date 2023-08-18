from django.shortcuts import render

# Create your views here.


def checkout_summary(request):
    return render(request, 'checkout/checkout-summary.html')


def checkout_add(request):
    pass


def checkout_delete(request):
    pass


def checkout_update(request):
    pass

