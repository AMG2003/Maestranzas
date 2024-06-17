from django.urls import path
from .views import home,base, exit, registro, perfil
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('logout/',exit,name="exit"),
    path('registro/',registro,name="registro"),
    path('perfil/',perfil,name="perfil"),
    path('registrar_pieza', views.registrar_pieza, name="registrar_pieza"),
    path('piezas/', views.lista_piezas,name="lista_piezas"),

]