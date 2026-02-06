from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Item

def home(request):
    total_items = Item.objects.count()
    found_count = Item.objects.filter(status='found').count()
    lost_count = Item.objects.filter(status='lost').count()
    recent_items = Item.objects.all().order_by('-date_created')[:6]
    
    context = {
        'total_items': total_items,
        'found_count': found_count,
        'lost_count': lost_count,
        'recent_items': recent_items,
    }
    return render(request, 'core/home.html', context)

def item_list(request):
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'found':
        items_list = Item.objects.filter(status='found')
    elif status_filter == 'lost':
        items_list = Item.objects.filter(status='lost')
    else:
        items_list = Item.objects.all()
    
    paginator = Paginator(items_list.order_by('-date_created'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'items': page_obj,
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1,
        'status_filter': status_filter,
    }
    return render(request, 'core/item_list.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'core/item_detail.html', context)