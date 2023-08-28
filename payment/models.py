from django.db import models

from django.contrib.auth.models import User

from shop.models import Product

class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250, null=True, blank=True)

    # Foreign Key to link user to shipping
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return 'Shipping Address -' + str(self.id)    


class Purchase(models.Model):

    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    shipping_address = models.TextField(max_length=5000)
    amount_purchased = models.DecimalField(max_digits=8, decimal_places=2)
    date_purchased = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return 'Order - #' + str(self.id)


class PurchaseItem(models.Model):
    # Foreign Keys 
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return 'Product Item - #' + str(self.id)




