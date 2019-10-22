from rest_framework import serializers

from ..models.situation_model import Situation


class SituationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Situation
        fields = ('situation_id', 'situation_name')
