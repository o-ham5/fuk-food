from rest_framework import serializers

from ..models.genre_model import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('genre_id', 'genre_name')
