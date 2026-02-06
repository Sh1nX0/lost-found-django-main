from django.contrib import admin
from .models import Item, Category, Location

# Регистрируем все модели
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'location', 'date_created']
    list_filter = ['status', 'category', 'location']
    search_fields = ['title', 'description', 'contact_info']
    list_per_page = 20
    
    # Если нужно добавить поле is_resolved, добавьте его в модель Item
    # или создайте вычисляемое свойство:
    
    def is_resolved(self, obj):
        """Вычисляемое поле (пример)"""
        return obj.status == 'found'
    is_resolved.boolean = True
    is_resolved.short_description = 'Решен'