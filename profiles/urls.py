from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("register-success", views.register_success, name="register-success"),
    # login logout urls
    path("my-login", views.my_login, name="my-login"),
    path("profile-logout", views.profile_logout, name="profile-logout"),
    path("pokemon_hub", views.pokemon_hub, name="pokemon-hub"),
    path(
        "profile-management",
        views.profile_management,
        name="profile-management",
    ),
    path("delete-profile", views.delete_profile, name="delete-profile"),
]
