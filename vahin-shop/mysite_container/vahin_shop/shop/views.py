from django.shortcuts import render
from django.http import HttpResponse

from .models import shop
from .models import Category

def index(request):
    shopz = shop.objects.all()
    categories = Category.objects.all()
    context = {
        'shop': shopz,
        'name': 'Товары',
        'categories': categories,
    }
    return render(request, template_name='shop/index.html', context=context)

def get_category(request, category_id):
    shopz = shop.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'shop/category.html', {'shop': shopz, 'categories': categories, 'category': category})