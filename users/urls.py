from multiprocessing.spawn import import_main_path
from unicodedata import name
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('about_me/', views.about_me, name='users-about_me'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),
         name='users-logout'),
]
