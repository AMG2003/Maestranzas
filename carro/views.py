from django.shortcuts import render
from .carro import Carro
from core.models import Pieza
from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, pieza_id):
    carro=Carro(request)
    pieza=Pieza.objects.get(id=pieza_id)
    carro.agregar(pieza=pieza)
    return redirect("carrito")

def eliminar_producto(request, pieza_id):
    carro=Carro(request)
    pieza=Pieza.objects.get(id=pieza_id)
    carro.eliminar(pieza=pieza)
    return redirect("carrito")

def restar_producto(request, pieza_id):
    carro=Carro(request)
    pieza=Pieza.objects.get(id=pieza_id)
    carro.restar_producto(pieza=pieza)
    return redirect("carrito")

def limpiar_Carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("home")