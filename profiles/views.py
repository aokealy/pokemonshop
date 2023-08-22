from django.shortcuts import render

from .forms import CreateUserForm

# Create your views here.

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()

            return redirect('')

    context = {'form':form}        

    return render(request,'profiles/registration/register.html', context=context)
