from django.conf.urls import include, url
from rest_framework import routers
from ..views.area_view import AreaRegister, AreaInfoGetView, AreaListGetView, AreaInfoUpdateView, AreaInfoDeleteView

urlpatterns = [
    url(r'^register/$', AreaRegister.as_view()),
    url(r'^list/$', AreaListGetView.as_view()),
    url(r'^info/(?P<area_id>[\w-]+)/$', AreaInfoGetView.as_view()),
    url(r'^update/(?P<area_id>[\w-]+)/$', AreaInfoUpdateView.as_view()),
    url(r'^delete/(?P<area_id>[\w-]+)/$', AreaInfoDeleteView.as_view()),
]
