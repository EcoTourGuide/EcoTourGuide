from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile-photo-upload/', views.profile_photo_upload, name='profile_photo_upload'),
    path('profile-information/', views.profile_information, name='profile_information'),
    path('user-history/', views.user_history, name='user_history'),
    path('newsletter-subscription/', views.newsletter_subscription, name='newsletter_subscription'),
    path('manage-notifications/', views.manage_notifications, name='manage_notifications'),
    path('record-visit/', views.record_visit, name='record_visit'),
]
