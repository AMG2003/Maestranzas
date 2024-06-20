from django.urls import path

from .import views

app_name="carro"

urlpatterns = [
    path("agregar/<int:pieza_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:pieza_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:pieza_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_Carro, name="limpiar")
]