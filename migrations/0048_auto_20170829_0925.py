# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0047_auto_20170826_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carico',
            name='q',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]