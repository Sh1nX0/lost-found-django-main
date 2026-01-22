from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Item, Category
from .forms import ItemForm

def home(request):
    recent_items = Item.objects.filter(is_resolved=False).order_by('-date_created')[:6]
    return render(request, 'core/home.html', {'recent_items': recent_items})

def item_list(request):
    items = Item.objects.filter(is_resolved=False).order_by('-date_created')
    status = request.GET.get('status')
    category_id = request.GET.get('category')
    search = request.GET.get('search')
    
    if status:
        items = items.filter(status=status)
    if category_id:
        items = items.filter(category_id=category_id)
    if search:
        items = items.filter(Q(titleicontains=search) | Q(descriptionicontains=search))
    
    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    
    return render(request, 'core/item_list.html', {'items': page_obj, 'categories': categories})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/item_detail.html', {'item': item})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'core/add_item.html', {'form': form})
