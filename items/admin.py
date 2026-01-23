from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'date', 'created_at')
    list_filter = ('type', 'date')
    search_fields = ('name', 'description', 'location')