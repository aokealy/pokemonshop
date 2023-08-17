from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name   


class Product(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=150, default='un-branded') 
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length=255) 
    image = models.ImageField(upload_to='images/')   

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    