# core/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Lost & Found Platform</h1><p>Главная страница</p>")

def item_list(request):
    return HttpResponse("<h1>Все предметы</h1><p>Список предметов будет здесь</p>")

def item_detail(request, pk):
    return HttpResponse(f"<h1>Детали предмета #{pk}</h1>")

def add_item(request):
    return HttpResponse("<h1>Добавить предмет</h1><p>Форма будет здесь</p>")