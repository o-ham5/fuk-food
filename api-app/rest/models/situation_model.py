from django.db import models
from django.core import validators
from django.utils import timezone


class Situation(models.Model):
    situation_id = models.AutoField(db_column='situation_id', primary_key=True)
    situation_name = models.CharField(
        db_column='situation name', max_length=30, unique=True)
    created_at = models.DateTimeField(
        db_column='created_at', default=timezone.now)
    updated_at = models.DateTimeField(
        db_column='updated_at', default=timezone.now)

    class Meta:
        db_table = 'situations'
