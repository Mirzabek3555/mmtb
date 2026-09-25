from django.contrib import admin
from .models import SiteSettings, Statistics, Announcement, Document


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'phone', 'email']


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['title', 'value', 'order']
    list_editable = ['order']


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title']
