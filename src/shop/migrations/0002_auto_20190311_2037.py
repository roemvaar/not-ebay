# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-12 03:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 20, 37, 41, 899081)),
        ),
    ]
