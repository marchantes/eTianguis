from django.conf.urls import url
from applications.views import IndexView, ProductCreate, UserCreate
from . import views

urlpatterns = [
    #url(r'^login/', views.user_login, name='login'),
    url(r'^signup/', UserCreate.as_view(), name='signup'),
    url(r'^product_create/', ProductCreate.as_view(), name='product_create'),
    url(r'^$', IndexView.as_view(), name='index'),
]