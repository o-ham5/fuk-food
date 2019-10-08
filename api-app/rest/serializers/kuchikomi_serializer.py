from rest_framework import serializers

from ..models.kuchikomi_model import Kuchikomi
from ..models.account_model import Account
from .account_serializer import AccountSerializer
from ..models.spot_model import Spot
from .spot_serializer import SpotSerializer
from ..models.situation_model import Situation
from .situation_serializer import SituationSerializer


class KuchikomiSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True)
    spot = SpotSerializer(read_only=True)
    spot_id = serializers.PrimaryKeyRelatedField(
        queryset=Spot.objects.all(), write_only=True)
    situation = SituationSerializer(read_only=True)
    situation_id = serializers.PrimaryKeyRelatedField(
        queryset=Situation.objects.all(), write_only=True)

    def create(self, validated_data):
        validated_data['account'] = validated_data.get('account_id', None)
        validated_data['spot'] = validated_data.get('spot_id', None)
        validated_data['situation'] = validated_data.get('situation_id', None)

        if validated_data['account'] is None:
            raise serializers.ValidationError('account not found')
        elif validated_data['spot'] is None:
            raise serializers.ValidationError('spot not found')
        elif validated_data['situation'] is None:
            raise serializers.ValidationError('situation not found')

        del validated_data['account_id']
        del validated_data['spot_id']
        del validated_data['situation_id']

        return Kuchikomi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['account'] = validated_data.get('account_id', None)
        validated_data['spot'] = validated_data.get('spot_id', None)
        validated_data['situation'] = validated_data.get('situation_id', None)

        if validated_data['account'] is None:
            raise serializers.ValidationError('account not found')
        elif validated_data['spot'] is None:
            raise serializers.ValidationError('spot not found')
        elif validated_data['situation'] is None:
            raise serializers.ValidationError('situation not found')

        del validated_data['account_id']
        del validated_data['spot_id']
        del validated_data['situation_id']

        try:
            instance.account = validated_data['account']
            instance.spot = validated_data['spot']
            instance.score = validated_data['situation']
            instance.score = validated_data['price']
            instance.score = validated_data['score']
            instance.comment = validated_data['comment']
        except KeyError:
            pass
        instance.save()

        return instance

    class Meta:
        model = Kuchikomi
        fields = ('kuchikomi_id', 'account',
                  'account_id', 'spot', 'spot_id', 'situation', 'situation_id', 'price', 'score', 'comment', 'created_at')
