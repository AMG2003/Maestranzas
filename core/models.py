from django.db import models

# Create your models here.

class Pieza(models.Model):
    descripcion = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()
    cantidad_minima = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.descripcion} ({self.numero_serie})'