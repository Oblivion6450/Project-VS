from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from .models import Product
from .models import Category

def index(request):
    shopz = Product.objects.all()
    context = {
        'shop': shopz,
        'name': 'Товары',
    }
    return render(request, template_name='shop/index.html', context=context)

def get_category(request, category_id):
    shopz = Product.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'shop/category.html', {'shop': shopz, 'category': category})

def view_shop(request, shop_id):
    shop_item = Product.objects.get(pk=shop_id)
    shop_item = get_object_or_404(Product, pk=shop_id)
    return render(request, 'shop/view_shop.html', {'shop_item': shop_item})

def detail_shop(request):
    cart_shop_form = CartAddProductForm()
    return render(request, 'templates/_card_shop.html', {'cart_shop_form': cart_shop_form})