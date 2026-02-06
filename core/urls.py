from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_api

# Создаем router для ViewSet
router = DefaultRouter()
router.register(r'items', views_api.ItemViewSet, basename='item')

urlpatterns = [
    # ===== HTML СТРАНИЦЫ =====
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    
    # ===== API ENDPOINTS =====
    # ViewSet маршруты (автоматически создает: /api/items/, /api/items/<pk>/)
    path('api/', include(router.urls)),
    
    # Дополнительные API endpoints
    path('api/stats/', views_api.item_stats, name='api-stats'),
    path('api/items-list/', views_api.ItemListAPIView.as_view(), name='api-item-list'),
    path('api/items/<int:pk>/', views_api.ItemDetailAPIView.as_view(), name='api-item-detail'),
]