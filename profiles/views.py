from django.shortcuts import redirect, render

from .forms import CreateUserForm




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



