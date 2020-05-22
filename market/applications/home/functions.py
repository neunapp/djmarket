#
from django.db.models import Prefetch, F, FloatField, ExpressionWrapper
#
from applications.venta.models import Sale, SaleDetail


def detalle_resumen_ventas(date_start, date_end):
    # funcion que recupera ventas no anuladas en rango de fechas
    # Y, el detalle de venta de cada venta
    
    if date_start and date_end:
        ventas = Sale.objects.ventas_en_fechas(date_start, date_end)
        consulta = ventas.prefetch_related(
            Prefetch(
                'detail_sale', 
                queryset=SaleDetail.objects.filter(sale__id__in=ventas).annotate(
                    subtotal=ExpressionWrapper(
                        F('price_sale')*F('count'),
                        output_field=FloatField()
                    )
                )
            )
        )

        return consulta
    else:
        return []
    