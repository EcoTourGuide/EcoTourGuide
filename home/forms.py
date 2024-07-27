# contact/forms.py

from django import forms
from .models import ContactMessage, Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
        error_messages = {
            'name': {
                'required': 'Name is required.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'message': {
                'required': 'Message is required.',
            },
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'review_title', 'review_text', 'date_of_visit', 'recommend']

        labels = {
            'rating': 'Rating: An integer between 1 (worst) and 5 (best)',
        }
        widgets = {
            'date_of_visit': forms.DateInput(attrs={'type': 'date', 'max': ''}),
        }