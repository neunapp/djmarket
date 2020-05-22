# python
from datetime import timedelta
# django
from django.utils import timezone
from django.db import models
#
from applications.producto.models import Product

from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper


class SaleManager(models.Manager):
    """ procedimiento para modelo venta """
    
    def ventas_no_cerradas(self):
        # creamos rango de fecha
        return self.filter(
            close=False,
            anulate=False
        )
    
    def total_ventas_dia(self):
        consulta = self.filter(
            close=False,
            anulate=False
        ).aggregate(
            total=Sum('amount')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0
    
    def total_ventas_anuladas_dia(self):
        consulta = self.filter(
            close=False,
            anulate=True
        ).aggregate(
            total=Sum('amount')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0
    
    def cerrar_ventas(self):
        consulta = self.filter(
            close=False,
        )
        # actualizmos a cerrado
        total = consulta.aggregate(
            total=Sum('amount')
        )['total']
        cerrados = consulta.update(close=True) # devuelve numero de actualizciones

        return cerrados, total
    
    def total_ventas(self):
        return self.filter(
            anulate=False,
        ).aggregate(
            total=Sum('amount')
        )['total']
    
    def ventas_en_fechas(self, date_start, date_end):
        return self.filter(
            anulate=False,
            date_sale__range=(date_start, date_end),
        ).order_by('-date_sale')



class SaleDetailManager(models.Manager):
    """ procedimiento modelo product """
    
    def detalle_por_venta(self, id_venta):
        return self.filter(
            sale__id=id_venta
        )

    def ventas_mes_producto(self, id_prod):
        # creamos rango de fecha
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30)
        
        consulta = self.filter(
            sale__anulate=False,
            created__range=(start_date, end_date),
            product__pk=id_prod,
        ).values('sale__date_sale__date', 'product__name').annotate(
            cantidad_vendida=Sum('count'),
        )
        return consulta
    
    def restablecer_stok_num_ventas(self, id_venta):
        prods_en_anulados = []
        for venta_detail in self.filter(sale__id=id_venta):
            #actualizmso producot
            venta_detail.product.count = venta_detail.product.count + venta_detail.count
            venta_detail.product.num_sale = venta_detail.product.num_sale - venta_detail.count
            prods_en_anulados.append(venta_detail.product)
        Product.objects.bulk_update(prods_en_anulados, ['count', 'num_sale'])
        return True
    
    def resumen_ventas(self):
        return self.filter(
            sale__anulate=False,
            sale__close=True,
        ).values('sale__date_sale__date').annotate(
            total_vendido=Sum(
                F('price_sale')*F('count'),
                output_field=FloatField()
            ),
            total_ganancias=Sum(
                F('price_sale')*F('count') - F('price_purchase')*F('count'),
                output_field=FloatField()
            ),
            num_ventas=Sum('count'),
        )
    
    def resumen_ventas_mes(self):
        #
        return self.filter(
            sale__anulate=False
        ).values('sale__date_sale__date__month', 'sale__date_sale__date__year').annotate(
            cantidad_ventas=Sum('count'),
            total_ventas=Sum(F('price_sale')*F('count'), output_field=FloatField()),
            ganancia_total=Sum(
                F('price_sale')*F('count') - F('price_purchase')*F('count'),
                output_field=FloatField()
            )
        ).order_by('-sale__date_sale__date__month')
    
    def resumen_ventas_proveedor(self, **filters):
        # recibe 3 parametros en un diccionario
        # devuelve lista de ventas en rango de fechas de un proveedor
        # y, devuelve el total de ventas en rango de fechas y de proveedor

        if filters['date_start'] and filters['date_end'] and filters['provider']:
            consulta = self.filter(
                anulate=False,
                sale__date_sale__range = (
                    filters['date_start'],
                    filters['date_end'],
                ),
                product__provider__pk=filters['provider'],
            )
            
            lista_ventas = consulta.annotate(
                sub_total=ExpressionWrapper(
                    F('price_purchase')*F('count'),
                    output_field=FloatField()
                )
            ).order_by('sale__date_sale')

            total_ventas = consulta.aggregate(
                total_venta=Sum(
                    F('price_purchase')*F('count'),
                    output_field=FloatField()
                )
            )['total_venta']

            return lista_ventas, total_ventas
        else:
            return [], 0



class CarShopManager(models.Manager):
    """ procedimiento modelo Carrito de compras """
    
    def total_cobrar(self):
        
        consulta = self.aggregate(
            total=Sum(
                F('count')*F('product__sale_price'),
                output_field=FloatField()
            ),
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0            

            