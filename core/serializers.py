from rest_framework import serializers
from .models import Item, Category, Location

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description']


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    date_created = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    
    class Meta:
        model = Item
        fields = [
            'id', 
            'title', 
            'description', 
            'status',
            'category',
            'location',
            'contact_info', 
            'date_created'
        ]
        read_only_fields = ['id', 'date_created']