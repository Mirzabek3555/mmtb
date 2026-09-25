from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'subject', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ['full_name', 'phone', 'subject']
    readonly_fields = ['full_name', 'phone', 'email', 'subject', 'message', 'created_at']
