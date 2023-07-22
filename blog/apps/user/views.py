from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from apps.user.forms import NewUserProfileForm
from django.contrib.auth import authenticate, login, logout

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = NewUserProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()

            # user = form.save(commit=False)
            # user.instance.user=request.user
            # user.save()
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') #claned_data sirve para obtener los datos del formulario
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                print('te logueaste')
                return redirect('index')
    context = {
        'form': form
    } 
    return render(request, 'auth/login.html', context)

def logoutUser(request):
    logout(request)
    print('te deslogueaste')
    return redirect('index')
    
    
def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('index')

    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/changePass.html', context)

