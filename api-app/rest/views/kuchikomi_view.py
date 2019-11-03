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
from ..models.account_model import Account

import numpy as np
from annoy import AnnoyIndex
from sklearn.preprocessing import StandardScaler

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

# ログインユーザと指定した相手の中点に近いユーザの口コミ情報リスト取得のView(GET)


class KuchikomiMedianListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KuchikomiSerializer

    def get_queryset(self):

        # request.dataで相手の性格を取得
        target_personality = np.array([
            float(self.request.query_params['inyou']),
            float(self.request.query_params['oshare']),
            float(self.request.query_params['shokuji']),
            float(self.request.query_params['setsuyaku'])
        ])
        # request.userでログインユーザの性格を取得
        login_user_personality = np.array([
            float(self.request.user.inyou),
            float(self.request.user.oshare),
            float(self.request.user.shokuji),
            float(self.request.user.setsuyaku)
        ])
        # 重みパラメータを利用して仮想のユーザデータを作成する
        weight = np.array([
            (100 - float(self.request.query_params['weight']))/100,
            (float(self.request.query_params['weight'])/100)
        ])
        virtual_user = np.average(
            np.vstack([target_personality, login_user_personality]),
            axis=0,
            weights=weight
        )
        # ログインユーザ以外の全ての他のアカウントを取得する
        accounts = Account.objects.exclude(
            account_id=self.request.user.account_id
        )
        # annoyに投げるnumpyデータを作成する
        data = virtual_user
        for account in accounts:
            candidate = np.array([
                float(account.inyou),
                float(account.oshare),
                float(account.shokuji),
                float(account.setsuyaku),
            ])
            data = np.vstack([data, candidate])
        # 標準化
        scaler = StandardScaler()
        scaler.fit(data)
        data = scaler.transform(data)
        # knn実行し、上位３名のアカウントIDを取得する。
        t = AnnoyIndex(data.shape[1], "euclidean")
        for i, v in enumerate(data):
            t.add_item(i, v)

        t.build(10)  # 10 trees
        result = t.get_nns_by_vector(virtual_user, 4, include_distances=False)

        # アカウントIDをクエリに、口コミ情報を取得する。
        queryset = []
        try:
            first = Kuchikomi.objects.filter(
                account=accounts[result[1]].account_id).order_by('-score')[0]
            first.account.account_id = None
            first.account.bias = None
            first.account.variance = None
            first.account.email = None
            queryset.append(first)
        except:
            pass
        try:
            second = Kuchikomi.objects.filter(
                account=accounts[result[2]].account_id).order_by('-score')[0]
            second.account.account_id = None
            second.account.bias = None
            second.account.variance = None
            second.account.email = None
            queryset.append(second)
        except:
            pass
        try:
            third = Kuchikomi.objects.filter(
                account=accounts[result[3]].account_id).order_by('-score')[0]
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
