from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = [
    #   Product endpoints
    url(r'^products/$', ProductsList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductsDetail.as_view()),

    #   User endpoints
    url(r'^users/$', UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UsersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
