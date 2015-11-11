from django.conf.urls import url
from applications.views import *

urlpatterns = [
    url(r'^login/', UserLogin.as_view(), name='login'),
    url(r'^signup/', UserCreate.as_view(), name='signup'),
    url(r'^logout/', UserLogout.as_view(), name='logout'),
    url(r'^product_list/', ProductList.as_view(), name='products'),
    url(r'^product_create/', ProductCreate.as_view(), name='product_create'),
    url(r'^product_detail/(?P<pk>[0-9]+)', ProductDetail.as_view(),
        name='product_detail'),
    url(r'^product_purchase/(?P<pk>[0-9]+)', ProductPurchase.as_view(),
        name='product_purchase'),
    url(r'^product_delete/(?P<pk>[0-9]+)', ProductDelete.as_view(),
        name='product_delete'),
    url(r'^purchases/', UserPurchases.as_view(), name="purchases"),
    url(r'^products/', UserProducts.as_view(), name="my_products"),
    url(r'^$', IndexView.as_view(), name='index'),
]
