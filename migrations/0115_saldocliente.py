# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0114_auto_20171226_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='saldocliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attivo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('passivo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestione.Cliente')),
            ],
        ),
    ]
