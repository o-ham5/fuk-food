from django.conf.urls import include, url
from rest_framework import routers
from ..views.kuchikomi_view import KuchikomiRegister, KuchikomiInfoGetView, KuchikomiListGetView, KuchikomiInfoUpdateView, KuchikomiInfoDeleteView, KuchikomiNeighborsListGetView

urlpatterns = [
    url(r'^register/$', KuchikomiRegister.as_view()),
    url(r'^list/$', KuchikomiListGetView.as_view()),
    url(r'^info/(?P<kuchikomi_id>[\w-]+)/$', KuchikomiInfoGetView.as_view()),
    url(r'^neighbors/$', KuchikomiNeighborsListGetView.as_view()),
    url(r'^update/(?P<kuchikomi_id>[\w-]+)/$',
        KuchikomiInfoUpdateView.as_view()),
    url(r'^delete/(?P<kuchikomi_id>[\w-]+)/$',
        KuchikomiInfoDeleteView.as_view()),
]
