# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alf_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='socio',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='pay_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
