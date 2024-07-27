# EcoTourGuideApp/urls.py

from django.urls import path
from . import views
from .views import aboutus

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/<int:page>/', views.fetch_destinations, name='explore'),
    path('explore/details/<int:destination_id>/', views.details, name='details'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('review/<int:destination_id>/', views.review, name='review'),
    path('get-suggestions/', views.get_suggestions, name='get_suggestions'),
    path('contactus/', views.contact_us, name='contactus'),
    path('support/', views.support, name='support'),
    path('terms-policies/', views.terms_policies, name='terms-policies'),

]
