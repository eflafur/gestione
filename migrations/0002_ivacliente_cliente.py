# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivacliente',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestione.Cliente'),
        ),
    ]
