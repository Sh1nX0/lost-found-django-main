from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Category, Location
from .serializers import ItemSerializer, CategorySerializer, LocationSerializer

# ViewSets для автоматического создания CRUD endpoints
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-date_created')
    serializer_class = ItemSerializer

# Дополнительный endpoint для статистики
@api_view(['GET'])
def item_stats(request):
    total = Item.objects.count()
    found = Item.objects.filter(status='found').count()
    lost = Item.objects.filter(status='lost').count()
    
    return Response({
        'total_items': total,
        'found_items': found,
        'lost_items': lost
    })