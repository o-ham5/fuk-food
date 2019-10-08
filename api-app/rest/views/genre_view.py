from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from ..serializers.genre_serializer import GenreSerializer
from ..models.genre_model import Genre

# ジャンル作成のView(POST)


class GenreRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ジャンル情報リスト取得のView(GET)


class GenreListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# ジャンル情報取得のView(GET)


class GenreInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# ジャンル情報更新のView(PUT)


class GenreInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GenreSerializer
    # lookup_field = 'email'
    queryset = Genre.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Genre.DoesNotExist:
            raise Http404

# ジャンル削除のView(DELETE)


class GenreInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GenreSerializer
    # lookup_field = 'email'
    queryset = Genre.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Genre.DoesNotExist:
            raise Http404
