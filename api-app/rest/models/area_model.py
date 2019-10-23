from django.db import models
from django.core import validators
from django.utils import timezone


class Area(models.Model):
    area_id = models.AutoField(db_column='area_id', primary_key=True)
    area_name = models.CharField(
        db_column='area_name', max_length=30, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'areas'
