# items/admin.py
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'location', 'date', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('title', 'description', 'location')
    ordering = ('-created_at',)