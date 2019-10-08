from rest_framework import serializers

from ..models.situation_model import Situation


class SituationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Situation
        fields = ('id', 'situation_name')
