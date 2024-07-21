from django.shortcuts import render, HttpResponse
from EcoTourGuide.firebase_config import db, auth, storage
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect('authentication:login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


def login_user(request):
    # GET request if user hits login.html
    # POST request if user submits the login form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Login User
            user = form.get_user()
            # messages.success(request, "You are now logged in.")
            login(request, user)
            return redirect('index')  # Redirect to homepage or another page where banner is displayed
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def index(request):
    return render(request, 'home/index.html')  # Path to the explorer template