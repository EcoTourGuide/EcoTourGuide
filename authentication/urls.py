# EcoTourGuideApp/urls.py

from django.urls import path
from . import views


app_name = 'authentication'

urlpatterns = [
   path('login/', views.login_user, name='login'),
   path('signup/', views.signup_user, name='signup'),
   path('logout/', views.logout_user, name='logout'),
   path('/login/forgot_password/', views.forgot_password, name='forgot_password'),
   path('', views.index, name='explorer'),  # URL pattern for the explorer page

]
