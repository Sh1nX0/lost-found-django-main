from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_api

router = DefaultRouter()
router.register(r'items', views_api.ItemViewSet)
router.register(r'categories', views_api.CategoryViewSet)
router.register(r'locations', views_api.LocationViewSet)

urlpatterns = [
    # HTML страницы
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/stats/', views_api.item_stats, name='api-stats'),
]