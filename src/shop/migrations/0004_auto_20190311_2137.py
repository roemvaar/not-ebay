# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-12 04:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190311_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 21, 37, 43, 5202)),
        ),
    ]