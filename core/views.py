from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Item

def home(request):
    total = Item.objects.count()
    found = Item.objects.filter(status='found').count()
    lost = Item.objects.filter(status='lost').count()
    recent = Item.objects.all().order_by('-date_created')[:6]
    
    context = {
        'total_items': total,
        'found_count': found,
        'lost_count': lost,
        'recent_items': recent,
    }
    return render(request, 'core/home.html', context)

def item_list(request):
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'found':
        items = Item.objects.filter(status='found')
    elif status_filter == 'lost':
        items = Item.objects.filter(status='lost')
    else:
        items = Item.objects.all()
    
    paginator = Paginator(items.order_by('-date_created'), 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    
    context = {
        'items': page_obj,
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1,
    }
    return render(request, 'core/item_list.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'core/item_detail.html', context)