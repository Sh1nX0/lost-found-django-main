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
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='location', write_only=True)
    
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'category', 'category_id', 'location', 'location_id', 'status', 'image', 'date_lost_found', 'date_created', 'user', 'contact_info', 'is_resolved']
        read_only_fields = ['user', 'date_created']