from django.urls import path
from .views import home,base, logout_usuario, registro_usuario,login_usuario, perfil, piezas,eliminar_pieza
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('logout/',logout_usuario,name="logout"),
    path('registro/',registro_usuario,name="registro"),
    path('login/', login_usuario, name="login"),
    path('perfil/',perfil,name="perfil"),
    path('registrar_pieza', views.registrar_pieza, name="registrar_pieza"),
    path('lista_piezas/', views.lista_piezas,name="lista_piezas"),
    path('piezas/',piezas, name="piezas"),
    path('eliminar_pieza/<int:id>',eliminar_pieza,name="eliminar_pieza"),
    path('pieza/<int:pieza_id>/', views.detalle_pieza, name='detalle_pieza'),
    path('carrito', views.carrito, name="carrito"),

]