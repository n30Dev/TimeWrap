from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password is incorrect')
            return render(request, 'login.html')

    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'login.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login/')

        data = {'form': form}

        return render(request, 'register.html', data)


def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')
