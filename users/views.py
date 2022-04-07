from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')

    else:
        form = SignUpForm()
        
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)
