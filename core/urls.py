from django.urls import path
from .views import home,base, exit, registro, perfil, piezas,eliminar_pieza
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('logout/',exit,name="exit"),
    path('registro/',registro,name="registro"),
    path('perfil/',perfil,name="perfil"),
    path('registrar_pieza', views.registrar_pieza, name="registrar_pieza"),
    path('lista_piezas/', views.lista_piezas,name="lista_piezas"),
    path('piezas/',piezas, name="piezas"),
    path('eliminar_pieza/<int:id>',eliminar_pieza,name="eliminar_pieza"),
    path('pieza/<int:pieza_id>/', views.detalle_pieza, name='detalle_pieza'),

]