from django.contrib import admin

# Register your models here.

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'created','updated']
    search_fields = ['__str__', 'price']
    list_editable = ['price']
    list_filter = ['price', 'created', 'updated']
admin.site.register(Product, ProductAdmin)
