from applications.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class ProductoSerializer(serializers.ModelSerializer):
    id_usuario = serializers.ReadOnlyField(source='id_usuario.username')

    class Meta:
        model = Producto
        fields = ('id', 'id_usuario', 'nombre', 'descripcion',
                  'imagen', 'precio', 'fecha_publicacion',
                  'cantidad')


class TransaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaccion
        fields = ('id', 'id_usuario', 'id_producto', 'fecha', 'cantidad')


class UserSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Producto.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'products')
