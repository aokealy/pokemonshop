from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import shop, product_information, list_category


class TestUrls(SimpleTestCase):
    def test_shop_url_is_resolves(self):
        url = reverse("shop")
        self.assertEquals(resolve(url).func, shop)

    def test_product_information_url_is_resolves(self):
        url = reverse("product-information", args=["some-slug"])
        self.assertEquals(resolve(url).func, product_information)

    def test_list_category_url_is_resolved(self):
        url = reverse("list-category", args=["some-slug1"])
        self.assertEquals(resolve(url).func, list_category)
