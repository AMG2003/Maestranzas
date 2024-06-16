from django.urls import path
from .views import home,base, exit, registro

urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('logout/',exit,name="exit"),
    path('registro/',registro,name="registro")
]