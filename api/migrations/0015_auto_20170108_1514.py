# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-08 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20170108_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventship',
            name='is_join',
            field=models.IntegerField(default=0),
        ),
    ]
