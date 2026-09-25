from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'school_type', 'number', 'director_name', 'student_count', 'teacher_count', 'is_active']
    list_editable = ['is_active']
    list_filter = ['school_type', 'is_active']
    search_fields = ['name', 'director_name', 'address']
