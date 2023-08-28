from django.shortcuts import render
from .models import ShippingAddress, Purchase, PurchaseItem
from checkout.checkout import Checkout
from django.http import JsonResponse

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

         # checkout info
        checkout = Checkout(request)

        # total price of items
        total_cost = checkout.get_total()

        # authenticated users for checkout when making purchase
        if request.user.is_authenticated:
            purchase = Purchase.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_purchased=total_cost,
                user=request.user,
            )
            purchase_id = purchase.pk

            for item in checkout:
                PurchaseItem.objects.create(
                    purchase_id=purchase_id,
                    product=item["product"],
                    quantity=item["qty"],
                    price=item["price"],
                    user=request.user,
                )
         # guest users checkout when placing order
        else:
            purchase = Purchase.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_purchased=total_cost,
            )

            purchase_id = purchase.pk

            for item in checkout:
                PurchaseItem.objects.create(
                    purchase_id=purchase_id,
                    product=item["product"],
                    quantity=item["qty"],
                    price=item["price"],
                )

        purchase_success = True
        response = JsonResponse({"success": purchase_success})

        return response


def payment_successful(request):
     # clear the cart when order complete

    for key in list(request.session.keys()):
        if key == "session_key":
            del request.session[key]

    return render(request, 'payment/payment-successful.html')


def payment_failure(request):
    return render(request, 'payment/payment-failure.html')    

    