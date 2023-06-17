from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='nome'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('shop/<int:shop_id>/', view_shop, name='view_shop'),
]