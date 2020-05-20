#
from django.utils import timezone
from django.db.models import Prefetch
#
from applications.producto.models import Product
#
from .models import Sale, SaleDetail, CarShop


def procesar_venta(self, **params_venta):
    # recupera la lista de productos en carrtio
    productos_en_car = CarShop.objects.all()
    if productos_en_car.count() > 0:
        
        # crea el objeto venta
        venta = Sale.objects.create(
            date_sale=timezone.now(),
            count=0,
            amount=0,
            type_invoce=params_venta['type_invoce'],
            type_payment=params_venta['type_payment'],
            user=params_venta['user'],
        )
        #
        ventas_detalle = []
        productos_en_venta = []
        for producto_car in productos_en_car:
            venta_detalle = SaleDetail(
                product=producto_car.product,
                sale=venta,
                count=producto_car.count,
                price_purchase=producto_car.product.purchase_price,
                price_sale=producto_car.product.sale_price,
                tax=0.18,
            )
            # actualizmos stok de producto en iteracion
            producto = producto_car.product
            producto.count = producto.count - producto_car.count
            producto.num_sale = producto.num_sale + producto_car.count
            #
            ventas_detalle.append(venta_detalle)
            productos_en_venta.append(producto)
            #
            venta.count = venta.count + producto_car.count
            venta.amount = venta.amount + producto_car.count*producto_car.product.sale_price

        venta.save()
        SaleDetail.objects.bulk_create(ventas_detalle)
        # actualizamos el stok
        Product.objects.bulk_update(productos_en_venta, ['count', 'num_sale'])
        # completada la venta, eliminamos productos delc arrito
        productos_en_car.delete()
        return venta
    else:
        return None
    