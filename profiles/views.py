from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm, UpdateUserForm

from django.contrib.auth.models import User

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            messages.success(request, "Registration was Successful")
            return redirect("register-success")

    context = {"form": form}

    return render(
        request, "profiles/registration/register.html", context=context
    )


def register_success(request):
    return render(request, "profiles/registration/register-success.html")


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                
                messages.info(request, "Login was Successful") 
                return redirect("pokemon-hub")

    context = {"form": form}

    return render(request, "profiles/my-login.html", context=context)


# logout
def profile_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == "session_key":
                continue

            else:
                del request.session[key]

    except KeyError:
        pass

    messages.success(request, "Logout was successful")

    return redirect("shop")


@login_required(login_url="my-login")
def pokemon_hub(request):
    return render(request, "profiles/pokemon-hub.html")


@login_required(login_url="my-login")
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.info(request, "Profile has been updated") 
            return redirect("pokemon-hub")

    context = {"user_form": user_form}

    return render(request, "profiles/profile-management.html", context=context)


@login_required(login_url="my-login")
def delete_profile(request):
    user = User.objects.get(id=request.user.id)

    if request.method == "POST":
        user.delete()
        
        messages.error(request, "Account has been deleted") 
        return redirect("shop")

    return render(request, "profiles/delete-profile.html")
