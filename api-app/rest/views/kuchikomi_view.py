from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from ..serializers.kuchikomi_serializer import KuchikomiSerializer
from ..models.kuchikomi_model import Kuchikomi
from ..models.neighborhood_model import Neighborhood

# 口コミ作成のView(POST)


class KuchikomiRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Kuchikomi.objects.all()
    serializer_class = KuchikomiSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = KuchikomiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 口コミ情報リスト取得のView(GET)


class KuchikomiListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Kuchikomi.objects.all()
    serializer_class = KuchikomiSerializer


# ログインユーザに似ているユーザの口コミ情報リスト取得のView(GET)

class KuchikomiNeighborsListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KuchikomiSerializer

    def get_queryset(self):
        neighborhood = Neighborhood.objects.all()
        neighbors = neighborhood.get(
            target=self.request.user.account_id)
        queryset = []
        try:
            first = Kuchikomi.objects.filter(
                account=neighbors.first.account_id).order_by('-score')[0]
            first.account.account_id = None
            first.account.bias = None
            first.account.variance = None
            first.account.email = None
            queryset.append(first)
        except:
            pass
        try:
            second = Kuchikomi.objects.filter(
                account=neighbors.second.account_id).order_by('-score')[0]
            second.account.account_id = None
            second.account.bias = None
            second.account.variance = None
            second.account.email = None
            queryset.append(second)
        except:
            pass
        try:
            third = Kuchikomi.objects.filter(
                account=neighbors.third.account_id).order_by('-score')[0]
            third.account.account_id = None
            third.account.bias = None
            third.account.variance = None
            third.account.email = None
            queryset.append(third)
        except:
            pass

        return queryset


# 口コミ情報取得のView(GET)


class KuchikomiInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Kuchikomi.objects.all()
    serializer_class = KuchikomiSerializer
    lookup_field = 'kuchikomi_id'
    lookup_url_kwarg = 'kuchikomi_id'

# 口コミ情報更新のView(PUT)


class KuchikomiInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KuchikomiSerializer
    queryset = Kuchikomi.objects.all()
    lookup_field = 'kuchikomi_id'
    lookup_url_kwarg = 'kuchikomi_id'

    # def get_object(self):
    #     try:
    #         instance = self.queryset.get(Kuchikomi_id=self.request.Kuchikomi_id)
    #         return instance
    #     except Kuchikomi.DoesNotExist:
    #         raise Http404

# 口コミ削除のView(DELETE)


class KuchikomiInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KuchikomiSerializer
    queryset = Kuchikomi.objects.all()
    lookup_field = 'kuchikomi_id'
    lookup_url_kwarg = 'kuchikomi_id'

    # def get_object(self):
    #     try:
    #         for key in self.request.__dict__.keys():
    #             print(key)
    #         instance = self.queryset.get(Kuchikomi_id=self.request.Kuchikomi_id)
    #         return instance
    #     except Kuchikomi.DoesNotExist:
    #         raise Http404
