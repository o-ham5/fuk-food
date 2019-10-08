from django.conf.urls import include, url
from rest_framework import routers
from ..views.situation_view import SituationRegister, SituationInfoGetView, SituationListGetView, SituationInfoUpdateView, SituationInfoDeleteView

urlpatterns = [
    url(r'^register/$', SituationRegister.as_view()),
    url(r'^list/$', SituationListGetView.as_view()),
    url(r'^info/(?P<id>[\w-]+)/$', SituationInfoGetView.as_view()),
    url(r'^update/(?P<id>[\w-]+)/$',
        SituationInfoUpdateView.as_view()),
    url(r'^delete/(?P<id>[\w-]+)/$',
        SituationInfoDeleteView.as_view()),
]
