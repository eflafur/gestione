# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0108_auto_20171129_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='carico',
            name='qn',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]