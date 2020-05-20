# disparadores
def update_stok_ventas_producto(sender, instance, **kwargs):
    producto = instance.product
    producto.num_sale = producto.num_sale + 1
    producto.count = producto.count - instance.count
    producto.save()
    return instance