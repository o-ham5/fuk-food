from django.db import models
from django.core import validators
from django.utils import timezone
from .genre_model import Genre
from .area_model import Area

import uuid


class Spot(models.Model):
    spot_id = models.AutoField(db_column='spot_id', primary_key=True)
    spot_name = models.CharField(
        db_column='spot_name', max_length=30, unique=True)
    area = models.ForeignKey(Area, db_column='area', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, db_column='genre',
                              on_delete=models.CASCADE)
    evaluated_score = models.FloatField(
        db_column='evaluated_score', default=3.0)
    latitude = models.FloatField(db_column='latitude', blank=True, null=True)
    longitude = models.FloatField(db_column='longitude', blank=True, null=True)
    link = models.URLField(db_column='link', blank=True, null=True)
    created_at = models.DateTimeField(
        db_column='created_at', default=timezone.now)
    updated_at = models.DateTimeField(
        db_column='updated_at', default=timezone.now)

    class Meta:
        db_table = 'spots'
