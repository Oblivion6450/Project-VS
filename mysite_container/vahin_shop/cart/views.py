from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import *


@require_POST
def cart_add(request, shop_id):
    cart = Cart(request)
    shop_item = get_object_or_404(shop, id=shop_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(shop=shop_item,
                 amount=cd['amount'],
                 update_amount=cd['update'])
    return redirect('/cart')
    

def cart_remove(request, shop_id):
    cart = Cart(request)
    shop_item = get_object_or_404(shop, id=shop_id)
    cart.remove(shop)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


