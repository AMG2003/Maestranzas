# from django.shortcuts import render
# from .carro import Carro
# from core.models import Pieza
# from django.shortcuts import redirect
# # Create your views here.

# def agregar_producto(request, pieza):
#     carro=Carro(request)
#     pieza=Pieza.objects.get(id=id)
#     carro.agregar(producto=producto)
#     return redirect("carrito")

# def eliminar_producto(request, producto_id):
#     carro=Carro(request)
#     producto=Producto.objects.get(cod_Producto=producto_id)
#     carro.eliminar(producto=producto)
#     return redirect("carrito")

# def restar_producto(request, producto_id):
#     carro=Carro(request)
#     producto=Producto.objects.get(cod_Producto=producto_id)
#     carro.restar_producto(producto=producto)
#     return redirect("carrito")

# def limpiar_Carro(request, producto_id):
#     carro=Carro(request)
#     carro.limpiar_carro()
#     return redirect("home")