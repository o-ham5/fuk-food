from django.db import models
from django.core import validators
from django.utils import timezone
from .genre_model import Genre
from .area_model import Area

import uuid


class Spot(models.Model):
    spot_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    spot_name = models.CharField('spot name', max_length=30, unique=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    evaluated_score = models.FloatField(default=3.0)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'spots'
