from django.conf.urls import include, url
from rest_framework import routers
from ..views.genre_view import GenreRegister, GenreInfoGetView, GenreListGetView, GenreInfoUpdateView, GenreInfoDeleteView

urlpatterns = [
    url(r'^register/$', GenreRegister.as_view()),
    url(r'^list/$', GenreListGetView.as_view()),
    url(r'^info/(?P<id>[\w-]+)/$', GenreInfoGetView.as_view()),
    url(r'^update/(?P<id>[\w-]+)/$', GenreInfoUpdateView.as_view()),
    url(r'^delete/(?P<id>[\w-]+)/$', GenreInfoDeleteView.as_view()),
]
