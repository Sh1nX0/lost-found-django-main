from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-date_created')  # ← Исправлено
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

class ItemListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        items = Item.objects.all().order_by('-date_created')  # ← Исправлено
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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