from django.contrib import admin
from .models import News, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_published', 'is_featured', 'views', 'created_at']
    list_editable = ['is_published', 'is_featured']
    list_filter = ['is_published', 'is_featured', 'category']
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
