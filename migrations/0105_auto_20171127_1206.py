# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-27 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0104_sito_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sito',
            name='comune',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
