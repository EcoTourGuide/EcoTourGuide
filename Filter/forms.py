from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'phone', 'location', 'profile_photo']

class ProfilePhotoForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=True)

    class Meta:
        model = UserProfile
        fields = ['profile_photo']
