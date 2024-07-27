from django.contrib import admin
from .models import TravelDestination, ContactMessage, TravelDestinationDetails, Review

admin.site.register(TravelDestination)
admin.site.register(TravelDestinationDetails)
admin.site.register(Review)
# admin.site.register(ContactMessage)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

