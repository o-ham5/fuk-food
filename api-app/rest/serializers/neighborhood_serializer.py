from rest_framework import serializers

from ..models.neighborhood_model import Neighborhood
from ..models.account_model import Account
from .account_serializer import AccountSerializer


class NeighborhoodSerializer(serializers.ModelSerializer):
    target = AccountSerializer(read_only=True)
    target_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True)
    first = AccountSerializer(read_only=True)
    first_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True)
    second = AccountSerializer(read_only=True)
    second_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True)
    third = AccountSerializer(read_only=True)
    third_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True)

    def create(self, validated_data):
        validated_data['target'] = validated_data.get('account_id', None)
        validated_data['first'] = validated_data.get('account_id', None)
        validated_data['second'] = validated_data.get('account_id', None)
        validated_data['third'] = validated_data.get('account_id', None)

        if validated_data['target'] is None:
            raise serializers.ValidationError('target not found')
        elif validated_data['first'] is None:
            raise serializers.ValidationError('first not found')
        elif validated_data['second'] is None:
            raise serializers.ValidationError('second not found')
        elif validated_data['third'] is None:
            raise serializers.ValidationError('third not found')

        del validated_data['target_id']
        del validated_data['first_id']
        del validated_data['second_id']
        del validated_data['third_id']

        return Neighborhood.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['target'] = validated_data.get('account_id', None)
        validated_data['first'] = validated_data.get('account_id', None)
        validated_data['second'] = validated_data.get('account_id', None)
        validated_data['third'] = validated_data.get('account_id', None)

        if validated_data['target'] is None:
            raise serializers.ValidationError('target not found')
        elif validated_data['first'] is None:
            raise serializers.ValidationError('first not found')
        elif validated_data['second'] is None:
            raise serializers.ValidationError('second not found')
        elif validated_data['third'] is None:
            raise serializers.ValidationError('third not found')

        del validated_data['target_id']
        del validated_data['first_id']
        del validated_data['second_id']
        del validated_data['third_id']

        try:
            instance.target = validated_data['area']
            instance.first = validated_data['first']
            instance.second = validated_data['second']
            instance.third = validated_data['third']
        except KeyError:
            pass
        instance.save()

        return instance

    class Meta:
        model = Neighborhood
        fields = ('neighborhood_id', 'target',
                  'target_id', 'first', 'first_id', 'second', 'second_id', 'third', 'third_id')
