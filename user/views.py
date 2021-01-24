from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth import authenticate


def register(request):
    register_form = UserRegisterForm()
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect('register')
    else:
        register_form = UserRegisterForm()

    context = {
        'register_form': register_form,
    }
    return render(request, 'user/register.html', context)