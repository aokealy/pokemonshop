from django.urls import path

from . import views

urlpatterns = [
    path("final-checkout", views.final_checkout, name="final-checkout"),
    path(
        "complete-purchase", views.complete_purchase, name="complete-purchase"
    ),
    path(
        "payment-successful",
        views.payment_successful,
        name="payment-successful",
    ),
    path("payment-failure", views.payment_failure, name="payment-failure"),
]
