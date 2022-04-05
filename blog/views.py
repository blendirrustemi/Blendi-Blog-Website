from turtle import pos
from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

# Create your views here.
def index(request):
    posts = PostModel.objects.all()

    return render(request, 'blog/index.html', {'posts': posts})

