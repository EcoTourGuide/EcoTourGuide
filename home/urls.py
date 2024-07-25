# EcoTourGuideApp/urls.py

from django.urls import path
from . import views
from .views import contact_view
from .views import aboutus

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/<int:page>/', views.fetch_destinations, name='explore'),
    path('support/', views.support, name='support'),
    path('terms-policies/', views.terms_policies, name='terms-policies'),
    path('contact/', views.contact_us, name='contact')
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contact_view, name='contactus'),
]
