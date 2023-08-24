from django.shortcuts import render

# Create your views here.

def payment_successful(request):
    return render(request, 'payment/payment-successful.html')

def payment_failure(request):
    return render(request, 'payment/payment-failure.html')    
