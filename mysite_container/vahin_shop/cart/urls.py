from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:shop_id>', views.cart_add, name='cart_add'),
    path('cart/remove/<int:shop_id>/', views.cart_remove, name='cart_remove'),
]