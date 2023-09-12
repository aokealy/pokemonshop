from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import (
    checkout_summary,
    checkout_add,
    checkout_delete,
    checkout_update,
)


class TestUrls(SimpleTestCase):
    def test_summary_url_is_resolves(self):
        url = reverse("checkout-summary")
        self.assertEquals(resolve(url).func, checkout_summary)

    def test_checkout_add_url_is_resolves(self):
        url = reverse("checkout-add")
        self.assertEquals(resolve(url).func, checkout_add)

    def test_checkout_delete_url_is_resolved(self):
        url = reverse("checkout-delete")
        self.assertEquals(resolve(url).func, checkout_delete)

    def test_checkout_update_url_is_resolved(self):
        url = reverse("checkout-update")
        self.assertEquals(resolve(url).func, checkout_update)
