from django.conf.urls import url
from applications.views import IndexView, ProductCreate, ProductList, UserCreate, UserLogin

urlpatterns = [
    url(r'^login/', UserLogin.as_view(), name='login'),
    url(r'^signup/', UserCreate.as_view(), name='signup'),
    url(r'^product_create/', ProductCreate.as_view(), name='product_create'),
    url(r'^product/', ProductList.as_view(), name='product'),
    url(r'^$', IndexView.as_view(), name='index'),
]