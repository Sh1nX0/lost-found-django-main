from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    
    class Meta:
        model = Item
        fields = [
            'id', 
            'title', 
            'description', 
            'status', 
            'category',  # Теперь просто CharField
            'location',  # Теперь просто CharField
            'contact_info', 
            'date_created'
        ]
        read_only_fields = ['id', 'date_created']