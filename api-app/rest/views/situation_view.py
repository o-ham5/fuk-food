from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from ..serializers.situation_serializer import SituationSerializer
from ..models.situation_model import Situation

# ジャンル作成のView(POST)


class SituationRegister(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Situation.objects.all()
    serializer_class = SituationSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = SituationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ジャンル情報リスト取得のView(GET)


class SituationListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Situation.objects.all()
    serializer_class = SituationSerializer


# ジャンル情報取得のView(GET)


class SituationInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Situation.objects.all()
    serializer_class = SituationSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# ジャンル情報更新のView(PUT)


class SituationInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SituationSerializer
    # lookup_field = 'email'
    queryset = Situation.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Situation.DoesNotExist:
            raise Http404

# ジャンル削除のView(DELETE)


class SituationInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SituationSerializer
    # lookup_field = 'email'
    queryset = Situation.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Situation.DoesNotExist:
            raise Http404
