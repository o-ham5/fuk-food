from django.conf.urls import include, url
from rest_framework import routers
from ..views.spot_view import SpotRegister, SpotInfoGetView, SpotListGetView, SpotTop3ListGetView, SpotInfoUpdateView, SpotInfoDeleteView

urlpatterns = [
    url(r'^register/$', SpotRegister.as_view()),
    url(r'^list/$', SpotListGetView.as_view()),
    url(r'^top3-list/$', SpotTop3ListGetView.as_view()),
    url(r'^info/(?P<spot_id>[\w-]+)/$', SpotInfoGetView.as_view()),
    url(r'^update/(?P<spot_id>[\w-]+)/$', SpotInfoUpdateView.as_view()),
    url(r'^delete/(?P<spot_id>[\w-]+)/$', SpotInfoDeleteView.as_view()),
]
