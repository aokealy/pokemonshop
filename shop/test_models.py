from django.test import TestCase
from shop.models import Product, Category

class TestModels(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name='category 1',
            slug='slug 1'

        )

    def test_category_is_assigned_slug_on_creation(self):
        self.assertEquals(self.category1.slug, 'category-1', 'slug-1')    

  