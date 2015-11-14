from rest_framework import generics, permissions
from applications.models import Producto
from api.serializers import ProductoSerializer, UserSerializer
from django.contrib.auth.models import User
from api.permissions import IsOwnerOrReadOnly


class ProductsList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(id_usuario=self.request.user)


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
