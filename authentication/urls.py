# EcoTourGuideApp/urls.py

from django.urls import path
from . import views


app_name = 'authentication'

urlpatterns = [
   path('login/', views.login_user, name='login'),
   path('signup/', views.signup_user, name='signup'),
   path('', views.index, name='explorer'),  # URL pattern for the explorer page

]
