from django.contrib import admin
from .models import Department, Staff


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'department', 'position', 'phone', 'is_management', 'order']
    list_editable = ['order', 'is_management']
    list_filter = ['department', 'is_management', 'position']
    search_fields = ['full_name', 'phone']
