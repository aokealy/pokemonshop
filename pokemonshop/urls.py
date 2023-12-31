"""pokemonshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


from django.conf.urls.static import static

urlpatterns = [
    # Admin url
    path('admin/', admin.site.urls),
    # Shop url
    path('', include('shop.urls')),
    # Checkout url
    path('checkout/', include('checkout.urls')),
    # profiles url 
    path('profiles/', include('profiles.urls')),
    # Payment urk
    path('payment/', include('payment.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pokemonshop.views.handler404'
