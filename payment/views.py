from django.shortcuts import render
from .models import ShippingAddress

# Create your views here.
def final_checkout(request):
    # User with account - pre fill the form

    if request.user.is_authenticated:
        try:
            # authenticated users with shipping info
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {"shipping": shipping_address}

            return render(request, "payment/final-checkout.html", context=context)

        except:
            # authenticated users with no shipping info
            return render(request, "payment/final-checkout.html")
    else:
        # guest user
         return render(request, 'payment/final-checkout.html')


def payment_successful(request):
    return render(request, 'payment/payment-successful.html')


def payment_failure(request):
    return render(request, 'payment/payment-failure.html')    


def complete_purchase(request):
    if request.POST.get("action") == "post":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        zipcode = request.POST.get("zipcode")

        # this is to style the shipping address
        shipping_address = (
            address1 + "\n" + address2 + "\n" + city + "\n" + zipcode + "\n"
        )
    