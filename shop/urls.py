from django.urls import path

from . import views

urlpatterns = [

    path('', views.shop, name='shop'),
    path('product/<slug:slug>/', views.product_information, name='product-information'),
    path('search/<slug:slug>/', views.list_category, name='list-category'),
]