# third-party
from model_utils.models import TimeStampedModel
# Django
from django.db import models
# local
from .managers import ProductManager

class Marca(TimeStampedModel):
    """
        Marca de un producto
    """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Provider(TimeStampedModel):
    """
        Proveedore de Producto
    """

    name = models.CharField(
        'Razon Social', 
        max_length=100
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefonos',
        max_length=40,
        blank=True,
    )
    web = models.URLField(
        'sitio web',
        blank=True,
    )


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    """
        Producto
    """

    UNIT_CHOICES = (
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    )

    barcode = models.CharField(
        max_length=13,
        unique=True
    )
    name = models.CharField(
        'Nombre', 
        max_length=40
    )
    provider = models.ForeignKey(
        Provider, 
        on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE
    )
    due_date = models.DateField(
        'fehca de vencimiento',
        blank=True, 
        null=True
    )
    description = models.TextField(
        'descripcion del producto',
        blank=True,
    )
    unit = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES, 
    )
    count = models.PositiveIntegerField(
        'cantidad en almacen',
        default=0
    )
    purchase_price = models.DecimalField(
        'precio compra',
        max_digits=7, 
        decimal_places=2
    )
    sale_price = models.DecimalField(
        'precio venta',
        max_digits=7, 
        decimal_places=2
    )
    num_sale = models.PositiveIntegerField(
        'numero de ventas',
        default=0
    )
    anulate = models.BooleanField(
        'eliminado',
        default=False
    )

    #
    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name




