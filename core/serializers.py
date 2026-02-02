from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """Сериализатор для предметов"""
    date_created = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Item
        fields = [
            'id', 
            'title', 
            'description', 
            'status', 
            'location', 
            'contact_info', 
            'image',
            'image_url',
            'date_created'
        ]
        read_only_fields = ['id', 'date_created']
    
    def get_image_url(self, obj):
        """Возвращает полный URL изображения"""
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None