from django.test import TestCase
from payment.models import ShippingAddress, Purchase, PurchaseItem

def test_shipping_address_string_method_returns_id(self):
    shippingaddress = ShippingAddress.objects.create(full_name='test shippingaddress')
    self.assertEquals(str(self.id), 'test shippingaddress')




    


