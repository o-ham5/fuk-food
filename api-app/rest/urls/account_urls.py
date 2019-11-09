from django.conf.urls import include, url
from rest_framework import routers
from ..views.account_view import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView, CheckExistingUserName, CheckExistingEmail

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^info/$', AuthInfoGetView.as_view()),
    url(r'^update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view()),
    url(r'^check-username/$', CheckExistingUserName.as_view()),
    url(r'^check-email/$', CheckExistingEmail.as_view()),
]
