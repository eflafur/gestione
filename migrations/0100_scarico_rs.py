# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-15 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0099_auto_20171114_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarico',
            name='rs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]
