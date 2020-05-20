from django.contrib import admin
#
from .models import Product, Marca, Provider


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'barcode',
        'provider',
        'marca',
        'due_date',
        'count',
        'purchase_price',
        'sale_price',
        'anulate',
    )
    search_fields = ('name', 'barcode', )
    list_filter = ('provider', 'marca', 'anulate',)


class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'web',
    )
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
#
admin.site.register(Provider, ProviderAdmin)
#
admin.site.register(Marca)
