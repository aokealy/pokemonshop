from django.test import SimpleTestCase
from django.urls import reverse, resolve
from payment.views import (
    final_checkout,
    complete_purchase,
    payment_successful,
    payment_failure,
)


class TestUrls(SimpleTestCase):
    def test_final_checkout_url_is_resolves(self):
        url = reverse("final-checkout")
        self.assertEquals(resolve(url).func, final_checkout)

    def test_complete_purchase_url_is_resolves(self):
        url = reverse("complete-purchase")
        self.assertEquals(resolve(url).func, complete_purchase)

    def test_payment_successful_url_is_resolved(self):
        url = reverse("payment-successful")
        self.assertEquals(resolve(url).func, payment_successful)

    def test_payment_failure_url_is_resolved(self):
        url = reverse("payment-failure")
        self.assertEquals(resolve(url).func, payment_failure)
