from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ Display the product details view"""
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """ Display programatic and human readable names"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
