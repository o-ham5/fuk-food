from rest_framework import serializers

from ..models.area_model import Area


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('area_id', 'area_name')
