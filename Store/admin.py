from django.contrib import admin
from .models.product import Product
from .models.category import Category


# Register your models here.
# This class will show name, price & category under Products instead of only Product
class AdminProduct(admin.ModelAdmin):
    list_display = ['category', 'name', 'price']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
