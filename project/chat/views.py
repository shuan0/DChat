from django.shortcuts import render

def home(request):
    return render(request, 'chat/home.html')

def profile(request):
    return render(request, 'chat/profile.html')
