from django.urls import path

from . import views

urlpatterns = [

    path('payment-successful', views.payment_successful, name='payment-successful'),

    path('payment-failure', views.payment_failure, name='payment-failure'),



]