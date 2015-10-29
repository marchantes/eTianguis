from django.contrib import admin
from applications.models import Producto

# Register your models here.

@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre','descripcion', 'imagen')
