from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm

# Create your views here.


def home(request):
    number=[1,2,4,5,6]
    name = 'Jenish'

    args={'name':name, 'numbers':number}
    return render(request, 'accounts/home.html', args, number)


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)

