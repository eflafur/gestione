# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0088_auto_20171012_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scarico',
            name='note',
            field=models.TextField(default='', max_length=30),
        ),
    ]