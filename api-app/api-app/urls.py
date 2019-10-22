"""api-app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin

urlpatterns = [
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/account/', include('rest.urls.account_urls')),
    url(r'^api/area/', include('rest.urls.area_urls')),
    url(r'^api/genre/', include('rest.urls.genre_urls')),
    url(r'^api/spot/', include('rest.urls.spot_urls')),
    url(r'^api/situation/', include('rest.urls.situation_urls')),
    url(r'^api/kuchikomi/', include('rest.urls.kuchikomi_urls')),
]
