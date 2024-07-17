# EcoTourGuideApp/urls.py

from django.urls import path
from . import views

app_name = 'Filter'

urlpatterns = [
    path('', views.index, name='index'),
]
