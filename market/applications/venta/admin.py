from django.contrib import admin
#
from .models import Sale, SaleDetail


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'date_sale',
        'count',
        'amount',
        'user',
        'close',
        'anulate',
    )
    list_filter = ('type_invoce', 'type_payment', 'anulate', 'user', )


class SaleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'sale',
        'count',
        'anulate',
    )
    search_fields = ('product__name',)


admin.site.register(Sale, SaleAdmin)
#
admin.site.register(SaleDetail, SaleDetailAdmin)
