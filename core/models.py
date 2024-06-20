from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
# Create your models here.

class Pieza(models.Model):
    descripcion = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()
    cantidad_minima = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_pieza = models.ImageField(null=True,blank=True,upload_to='pieza_fotos/')

    def __str__(self):
        return f'{self.descripcion} ({self.numero_serie})'
    
class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre_proyecto
    
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255)
    detalles_contacto = models.TextField()
    terminos_pago = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proveedor
    
class OrdenCompra(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado')
    ]
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'Orden {self.id} - {self.proveedor.nombre_proveedor}'
    
class DetalleOrdenCompra(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_recepcion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Detalle {self.id} - {self.orden_compra.id}'
    
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nombre, password, **extra_fields)
    
class Usuario(AbstractBaseUser):
    ROL_CHOICES = [
        ('Administrador del Sistema', 'Administrador del Sistema'),
        ('Gestor de Inventario', 'Gestor de Inventario'),
        ('Comprador', 'Comprador'),
        ('Almacén', 'Almacén'),
        ('Jefe de Producción', 'Jefe de Producción'),
        ('Auditor de Inventario', 'Auditor de Inventario'),
        ('Gerente de Proyectos', 'Gerente de Proyectos'),
        ('Usuario Final', 'Usuario Final')
    ]
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, default='Sin Apellido')
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(default=now)
    imagen_perfil = models.ImageField(default='Perfil.png',upload_to='users/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    
class Lote(models.Model):
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_recepcion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Lote {self.id} - {self.pieza.descripcion}'
    
class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
        ('Transferencia', 'Transferencia')
    ]
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50, choices=TIPO_CHOICES)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'Movimiento {self.id} - {self.tipo_movimiento} - {self.pieza.descripcion}'