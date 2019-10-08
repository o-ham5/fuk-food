from django.db import models
from django.core import validators
from django.utils import timezone
from .spot_model import Spot
from .account_model import Account
from .situation_model import Situation

import uuid


class Kuchikomi(models.Model):
    kuchikomi_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    price = models.FloatField()
    score = models.FloatField()
    comment = models.TextField(blank=True, null=True, max_length=1000)
    deviation = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    db_table = 'kuchikomis'
