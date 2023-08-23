from django.urls import path

from . import views

urlpatterns = [

     path('register', views.register, name='register'),

     path('email-verify', views.email_verify, name='email-verify'),  

     path('email-verify-sent', views.email_verify_sent, name='email-verify-sent'),    

     path('email-verify-success', views.email_verify_success, name='email-verifiy-success'),    

     path('email-verify-failed', views.email_verify_failed, name='email-verify-failed'), 

      # login logout urls

    path('my-login', views.my_login, name='my-login'),

    path('profile-logout', views.profile_logout, name='profile-logout'),

    path('pokemon_hub', views.pokemon_hub, name='pokemon-hub'), 

    path('profile-management', views.profile_management, name='profile-management'), 

    path('delete-profile', views.delete_profile, name='delete-profile'), 


    
]