from django.db import models
from django.contrib.auth.models import User
import datetime

class Producto(models.Model):
    id_usuario = models.ForeignKey(User, default=1)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(null=True, blank=True)
    precio = models.PositiveIntegerField()
    fecha_publicacion = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    id_producto = models.ForeignKey('Producto')
    id_usuario = models.ForeignKey(User)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
