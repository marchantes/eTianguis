from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    appellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Producto(models.Model):
    id_usuario = models.ForeignKey('Usuario')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField()
    precio = models.PositiveIntegerField()

class Transaccion(models.Model):
    id_producto = models.ForeignKey('Producto')
    id_usuario = models.ForeignKey('Usuario')
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
