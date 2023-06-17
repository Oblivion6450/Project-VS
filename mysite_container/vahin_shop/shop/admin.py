from django.contrib import admin

from .models import Product
from .models import Category

class shopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'status', 'price', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('category', 'status', 'published')
    list_filter = ('category', 'status', 'published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'title')
    list_display_links = ('category_id', 'title')
    search_fields = ('title',)

admin.site.register(Product, shopAdmin)
admin.site.register(Category)