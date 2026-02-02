from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """ViewSet для предметов"""
    queryset = Item.objects.all().order_by('-date_created')
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

class ItemListAPIView(APIView):
    """API для списка предметов"""
    
    def get(self, request):
        items = Item.objects.all().order_by('-date_created')
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def item_stats(request):
    """Статистика предметов"""
    total = Item.objects.count()
    found = Item.objects.filter(status='found').count()
    lost = Item.objects.filter(status='lost').count()
    
    return Response({
        'total_items': total,
        'found_items': found,
        'lost_items': lost
    })