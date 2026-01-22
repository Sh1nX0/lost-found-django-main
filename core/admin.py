from django.contrib import admin
from .models import Category, Location, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'location', 'date_created', 'is_resolved')
    list_filter = ('status', 'category', 'is_resolved')
    search_fields = ('title', 'description')