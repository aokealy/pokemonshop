from django.urls import path

from . import views

urlpatterns = [

    path('', views.checkout_summary, name='checkout-summary'),

    path('add/', views.cart_checkout, name='checkout-add'),

    path('delete/', views.checkout_delete, name='checkout-delete'),

    path('update/', views.checkout_update, name='checkout-update'),
]