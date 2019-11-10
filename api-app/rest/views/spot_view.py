from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from ..serializers.spot_serializer import SpotSerializer
from ..models.spot_model import Spot

# スポット作成のView(POST)


class SpotRegister(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# スポット情報リスト取得のView(GET)


class SpotListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


# スポットトップ３リスト取得のView(GET)


class SpotTop3ListGetView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SpotSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        print(bool(self.request.query_params))
        if bool(self.request.query_params):
            keys = self.request.query_params.keys()
            if ('area_id' in keys and 'genre_id' in keys):
                return queryset.filter(
                    area=self.request.query_params['area_id'],
                    genre=self.request.query_params['genre_id']
                ).order_by('-evaluated_score')
            elif ('area_id' in keys and 'genre_id' not in keys):
                return queryset.filter(
                    area=self.request.query_params['area_id'],
                ).order_by('-evaluated_score')
            elif ('area_id' not in keys and 'genre_id' in keys):
                return queryset.filter(
                    genre=self.request.query_params['genre_id']
                ).order_by('-evaluated_score')
        else:
            return queryset.order_by('-evaluated_score')


# スポット情報取得のView(GET)


class SpotInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    lookup_field = 'spot_id'
    lookup_url_kwarg = 'spot_id'

# スポット情報更新のView(PUT)


class SpotInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()
    lookup_field = 'spot_id'
    lookup_url_kwarg = 'spot_id'

    # def get_object(self):
    #     try:
    #         instance = self.queryset.get(spot_id=self.request.spot_id)
    #         return instance
    #     except Spot.DoesNotExist:
    #         raise Http404

# スポット削除のView(DELETE)


class SpotInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()
    lookup_field = 'spot_id'
    lookup_url_kwarg = 'spot_id'

    # def get_object(self):
    #     try:
    #         for key in self.request.__dict__.keys():
    #             print(key)
    #         instance = self.queryset.get(spot_id=self.request.spot_id)
    #         return instance
    #     except Spot.DoesNotExist:
    #         raise Http404
