from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = [
    url(r'^products/$', ProductsList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
