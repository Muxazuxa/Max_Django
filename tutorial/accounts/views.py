from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
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


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)



