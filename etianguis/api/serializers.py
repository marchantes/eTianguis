from applications.models import *
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'id_usuario', 'nombre', 'descripcion',
                  'imagen', 'precio', 'fecha_publicacion',
                  'cantidad')
