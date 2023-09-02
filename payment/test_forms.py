from django.test import TestCase
from .forms import ShippingForm


class TestShippingForm(TestCase):

    def test_shipping_name_is_required(self):

        form = ShippingForm({'full_name': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')


    def test_fields_are_explicit_in_form_metaclass(self):
        form = ShippingForm()
        self.assertEqual(form.Meta.fields, ['full_name', 'email', 'address1', 'address2', 'city', 'zipcode'])
    




    
    




 
