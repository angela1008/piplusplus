# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-07 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170107_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Discussion'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Group'),
        ),
    ]