# filter/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('user-history/', views.user_history, name='user_history'),
    path('record-visit/', views.record_visit, name='record_visit'),
]
