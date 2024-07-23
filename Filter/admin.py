from django.contrib import admin
from .models import UserProfile,History,UnsplashImage

# Register the UserProfile model
admin.site.register(UserProfile)
admin.site.register(History)
admin.site.register(UnsplashImage)

