from django.contrib import admin
from . models import ShippingAddress, Purchase, PurchaseItem
# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)

