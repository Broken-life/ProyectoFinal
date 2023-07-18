from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from apps.user.forms import NewUserProfileForm
from django.contrib.auth import authenticate, login, logout

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = NewUserProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)