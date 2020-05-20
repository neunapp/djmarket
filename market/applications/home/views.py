from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)
from applications.venta.models import Sale, SaleDetail
from applications.producto.models import Product


class PanelHomeView(TemplateView):
    template_name = "home/index.html"


# Create your views here.
class PanelAdminView(TemplateView):
    template_name = "home/administrador.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_ventas"] = Sale.objects.total_ventas_dia()
        context["total_anulaciones"] = Sale.objects.total_ventas_anuladas_dia()
        context["stok_cero"] = Product.objects.productos_en_cero().count()
        context["resumen_semana"] = SaleDetail.objects.resumen_ventas()[:7]
        return context
    