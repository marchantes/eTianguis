from django.contrib import admin
from applications.models import Producto

# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['nombre',
                                        'descripcion',
                                        'imagen',
                                        'precio']})
    ]
    list_display = ('id_usuario', 'id', 'nombre',
                    'descripcion', 'imagen', 'cantidad', 'precio',
                    'fecha_publicacion')
