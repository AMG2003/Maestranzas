from django.contrib import admin
from .models import Pieza, Proyecto, Proveedor, OrdenCompra, DetalleOrdenCompra \
, Usuario, Lote, MovimientoInventario

# Register your models here.
admin.site.register(Pieza)
admin.site.register(Proyecto)
admin.site.register(Proveedor)
admin.site.register(OrdenCompra)
admin.site.register(DetalleOrdenCompra)
admin.site.register(Usuario)
admin.site.register(Lote)
admin.site.register(MovimientoInventario)
