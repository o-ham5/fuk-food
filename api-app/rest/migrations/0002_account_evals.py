# Generated by Django 2.2.5 on 2019-10-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='evals',
            field=models.FloatField(default=0),
        ),
    ]
