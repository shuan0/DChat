from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def signup(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'GET':
        return render(request, 'account/signup.html', {'mcode': 0})

    username = request.POST['username']
    password_a = request.POST['password-a']
    password_b = request.POST['password-b']
    if password_a != password_b:
        return render(request, 'account/signup.html', {'mcode': 1})

    try:
        User.objects.get(username=username)
        return render(request, 'account/signup.html', {'mcode': 2})
    except:
        User.objects.create_user(username=username, password=password_a)

    return render(request, 'account/signup.html', {'mcode': 3})

def signin(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'GET':
        return render(request, 'account/signin.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, 'account/signin.html', {'mcode': 4})

    login(request, user)
    return redirect('home')
