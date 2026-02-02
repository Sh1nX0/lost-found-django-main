from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_api

router = DefaultRouter()
router.register(r'api/items', views_api.ItemViewSet)

urlpatterns = [
    # HTML страницы
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    
    # API
    path('api/', include(router.urls)),
    path('api/stats/', views_api.item_stats, name='api-stats'),
    path('api/items-list/', views_api.ItemListAPIView.as_view(), name='api-item-list'),
]