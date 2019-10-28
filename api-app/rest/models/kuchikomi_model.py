from django.db import models
from django.core import validators
from django.utils import timezone
from .spot_model import Spot
from .account_model import Account
from .situation_model import Situation

import uuid


class Kuchikomi(models.Model):
    kuchikomi_id = models.AutoField(db_column='kuchikomi_id', primary_key=True)
    account = models.ForeignKey(
        Account, db_column='account', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, db_column='spot', on_delete=models.CASCADE)
    situation = models.ForeignKey(
        Situation, db_column='situation', on_delete=models.CASCADE)
    price = models.FloatField(db_column='price')
    score = models.FloatField(db_column='score')
    comment = models.TextField(
        db_column='comment', blank=True, null=True, max_length=1000)
    deviation = models.FloatField(db_column='deviation', blank=True, null=True)
    created_at = models.DateTimeField(
        db_column='created_at', default=timezone.now)
    updated_at = models.DateTimeField(
        db_column='updated_at', default=timezone.now)

    class Meta:
        db_table = 'kuchikomis'
