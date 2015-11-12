from rest_framework import generics
from applications.models import Producto
from api.serializers import ProductoSerializer


class ProductsList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
