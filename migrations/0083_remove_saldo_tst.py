# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0082_saldo_tst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saldo',
            name='tst',
        ),
    ]