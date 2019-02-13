from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

