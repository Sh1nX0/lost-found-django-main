# core/urls.py - УПРОЩЕННАЯ ВЕРСИЯ
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
]