from django.contrib import admin

# Register your models here.
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')  # Display these fields in the list view
    list_filter = ('timestamp',)  # Add a filter by timestamp
    search_fields = ('name', 'email', 'subject', 'message')  # Add a search box for these fields
    actions = ['delete_selected']  # Enable the delete action

admin.site.register(ContactMessage, ContactMessageAdmin)