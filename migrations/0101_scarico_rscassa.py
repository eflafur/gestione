# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-17 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0100_scarico_rs'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarico',
            name='rscassa',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]