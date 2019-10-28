from django.db import models
from django.core import validators
from django.utils import timezone
from .account_model import Account


class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(
        db_column='neighborhood_id', primary_key=True)
    target = models.ForeignKey(
        Account, db_column='target', on_delete=models.CASCADE, related_name='target')
    first = models.ForeignKey(
        Account, db_column='first', on_delete=models.CASCADE, related_name='first')
    second = models.ForeignKey(
        Account, db_column='second', on_delete=models.CASCADE, related_name='second')
    third = models.ForeignKey(
        Account, db_column='third', on_delete=models.CASCADE, related_name='third')
    created_at = models.DateTimeField(
        db_column='created_at', default=timezone.now)
    updated_at = models.DateTimeField(
        db_column='updated_at', default=timezone.now)

    class Meta:
        db_table = 'neighborhoods'
