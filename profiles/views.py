from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import User

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()

            return redirect('shop')

    context = {'form':form}        

    return render(request,'profiles/registration/register.html', context=context)

def email_verify(request):
    pass


def email_verify_sent(request):

    pass

def email_verify_success(request):

    pass


def email_verify_failed(request):

    pass



def my_login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("pokemon-hub")


    context = {'form':form}

    return render(request, 'profiles/my-login.html', context=context)





def pokemon_hub(request):
    return render(request, 'profiles/pokemon-hub.html')  
    
