from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import serializers
from ..models.spot_model import Spot

# FilterSetを継承したフィルタセット(設定クラス)を作る


class SpotFilter(filters.FilterSet):

    # フィルタの定義
    spot_id = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Spot
        fields = ['car_id', 'spot_id']
