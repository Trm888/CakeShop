from django.contrib import admin

from .models import CatalogCake, CustomCake


@admin.register(CatalogCake)
class CatalogCakeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
    ]


@admin.register(CustomCake)
class CustomCakeAdmin(admin.ModelAdmin):
    list_display = [
        'levels',
        'shape',
        'topping',
        'berries',
        'decor',
        'message',
        'get_total_price'
    ]
