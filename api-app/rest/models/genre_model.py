from django.db import models
from django.core import validators
from django.utils import timezone


class Genre(models.Model):
    genre_name = models.CharField('genre name', max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genres'
