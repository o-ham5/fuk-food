from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission

from ..serializers.area_serializer import AreaSerializer
from ..models.area_model import Area


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request)
        return request.user and request.user.is_admin == 1

# ジャンル作成のView(POST)


class AreaRegister(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ジャンル情報リスト取得のView(GET)


class AreaListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


# ジャンル情報取得のView(GET)


class AreaInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# ジャンル情報更新のView(PUT)


class AreaInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AreaSerializer
    # lookup_field = 'email'
    queryset = Area.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Area.DoesNotExist:
            raise Http404

# ジャンル削除のView(DELETE)


class AreaInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AreaSerializer
    # lookup_field = 'email'
    queryset = Area.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Area.DoesNotExist:
            raise Http404
