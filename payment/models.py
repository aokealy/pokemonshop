from django.db import models

from django.contrib.auth.models import User

class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250, null=True, blank=True)
