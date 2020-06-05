# django
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    TemplateView
)
#
from applications.venta.models import Sale, SaleDetail
from applications.users.mixins import VentasPermisoMixin
#
from .models import CloseBox
from .functions import detalle_ventas_no_cerradas


class ReporteCierreCajaView(VentasPermisoMixin, TemplateView):

    template_name = 'caja/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ventas_dia"] = detalle_ventas_no_cerradas
        context["total_vendido"] = Sale.objects.total_ventas_dia()
        context["total_anulado"] = Sale.objects.total_ventas_anuladas_dia()
        context["num_ventas_hoy"] = Sale.objects.ventas_no_cerradas().count()
        return context


class ProcesoCerrarCajaView(VentasPermisoMixin, View):

    def post(self, request, *args, **kwargs):
        # cerramos las ventas
        num_cerradas, total = Sale.objects.cerrar_ventas()
        if num_cerradas > 0:
            CloseBox.objects.create(
                date_close=timezone.now(),
                count=num_cerradas,
                amount= total,
                user=self.request.user
            )
        
        return HttpResponseRedirect(
            reverse(
                'caja_app:caja-index'
            )
        )
    
