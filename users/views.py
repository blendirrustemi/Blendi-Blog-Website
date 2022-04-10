from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def about_me(request):
    return render(request, 'users/about_me.html')
