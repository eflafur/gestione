# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0117_auto_20180104_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcod',
            name='cod',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
