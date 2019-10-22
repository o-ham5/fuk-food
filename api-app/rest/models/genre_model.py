from django.db import models
from django.core import validators
from django.utils import timezone


class Genre(models.Model):
    genre_id = models.AutoField(db_column='genre_id', primary_key=True)
    genre_name = models.CharField(
        db_column='genre name', max_length=30, unique=True)
    created_at = models.DateTimeField(
        db_column='created_at', default=timezone.now)
    updated_at = models.DateTimeField(
        db_column='updated_at', default=timezone.now)

    class Meta:
        db_table = 'genres'
