from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'What should we call you?',
            'email': "What's your email?",
            'password1': 'Create a password',
            'password2': 'Confirm password',
        }

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValidationError("Use 8 or more characters with a mix of letters, numbers & symbols.")
        return password
