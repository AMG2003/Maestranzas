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
    path('lista_usuarios/', views.lista_usuarios, name="lista_usuarios"),
    path('update_users/<int:id>',views.update_users,name="update_users"),
    path('datos_user/',views.datos_user,name="datos_user"),
    path('eliminar_usuario/<int:id>',views.eliminar_usuario,name="eliminar_usuario")

]