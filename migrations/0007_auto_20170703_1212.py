# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0006_auto_20170703_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produttore',
            name='azienda',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
