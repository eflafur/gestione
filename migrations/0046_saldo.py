# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0045_auto_20170816_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('data', models.DateField(default=datetime.date.today)),
                ('idcod', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
