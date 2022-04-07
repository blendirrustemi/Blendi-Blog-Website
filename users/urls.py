import imp
from multiprocessing.spawn import import_main_path
from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
]
