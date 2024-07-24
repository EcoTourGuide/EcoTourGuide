from django.contrib import admin
from .models import TravelDestination, ContactMessage

admin.site.register(TravelDestination)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    
