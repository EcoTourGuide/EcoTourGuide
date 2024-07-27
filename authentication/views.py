# authentication/views.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

from .forms import CustomUserCreationForm, CustomAuthenticationForm  # Import your custom form


def signup_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect('authentication:login')  # Redirect to login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            remember_me = form.cleaned_data.get('remember_me')
            if remember_me:
                request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days
            else:
                request.session.set_expiry(0)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('authentication:login')


def index(request):
    return render(request, 'home/index.html')


def forgot_password(request):
    return render(request, 'authentication/password_reset_form.html',)