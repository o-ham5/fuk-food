from rest_framework import serializers

from ..models.spot_model import Spot
from ..models.area_model import Area
from ..models.genre_model import Genre
from .area_serializer import AreaSerializer
from .genre_serializer import GenreSerializer


class SpotSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), write_only=True)
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), write_only=True)

    def create(self, validated_data):
        validated_data['area'] = validated_data.get('area_id', None)
        validated_data['genre'] = validated_data.get('genre_id', None)

        if validated_data['area'] is None:
            raise serializers.ValidationError('area not found')
        elif validated_data['genre'] is None:
            raise serializers.ValidationError('genre not found')

        del validated_data['area_id']
        del validated_data['genre_id']

        return Spot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['area'] = validated_data.get('area_id', None)
        validated_data['genre'] = validated_data.get('genre_id', None)
        print(validated_data)

        if validated_data['area'] is None:
            raise serializers.ValidationError('area not found')
        elif validated_data['genre'] is None:
            raise serializers.ValidationError('genre not found')

        del validated_data['area_id']
        del validated_data['genre_id']

        try:
            instance.spot_name = validated_data['spot_name']
            instance.area = validated_data['area']
            instance.genre = validated_data['genre']
            instance.latitude = validated_data['latitude']
            instance.longitude = validated_data['longitude']
            instance.link = validated_data['link']
            instance.evaluated_score = validated_data['evaluated_score']
        except KeyError:
            pass
        instance.save()

        return instance

    class Meta:
        model = Spot
        # fields = ('spot_id', 'spot_name', 'area',
        #           'area_id', 'genre', 'genre_id', 'score')
        fields = ('spot_id', 'spot_name', 'area',
                  'area_id', 'genre', 'genre_id', 'latitude', 'longitude', 'link', 'evaluated_score')
