# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-25 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0102_auto_20171122_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trasporto',
            name='lotto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
