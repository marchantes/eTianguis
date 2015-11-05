from django.conf.urls import url
from applications.views import IndexView, ProductCreate
from . import views

urlpatterns = [
    #url(r'^login/', views.user_login, name='login'),
    #url(r'^signup/', views.user_signup, name='signup'),
    url(r'^product_create/', ProductCreate.as_view(), name='product_create'),
    url(r'^$', IndexView.as_view(), name='index'),
]