# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0031_carico_bolla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcod',
            name='cod',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
