from django.shortcuts import render
from .checkout import Checkout
from shop.models import Product
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Create your views here.


def checkout_summary(request):
    checkout = Checkout(request)

    return render(
        request, "checkout/checkout-summary.html", {"checkout": checkout}
    )


def checkout_add(request):
    """This is where we add product to checkout"""
    checkout = Checkout(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        product = get_object_or_404(Product, id=product_id)

        checkout.add(product=product, product_qty=product_quantity)

        checkout_quantity = checkout.__len__()

        response = JsonResponse({"qty": checkout_quantity})

        return response


def checkout_delete(request):
    checkout = Checkout(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))

        checkout.delete(product=product_id)

        checkout_quantity = checkout.__len__()

        checkout_total = checkout.get_total()

        response = JsonResponse(
            {"qty": checkout_quantity, "total": checkout_total}
        )

        return response


def checkout_update(request):
    checkout = Checkout(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        checkout.update(product=product_id, qty=product_quantity)

        checkout_quantity = checkout.__len__()

        checkout_total = checkout.get_total()

        response = JsonResponse(
            {"qty": checkout_quantity, "total": checkout_total}
        )

        return response
