# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0118_auto_20180104_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExCsBl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('trasporto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('vari', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='carico',
            name='excsbl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestione.ExCsBl'),
        ),
    ]
