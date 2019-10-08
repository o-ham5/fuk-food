from django.conf.urls import include, url
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^user-info/$', AuthInfoGetView.as_view()),
    url(r'^auth-update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view()),
]
