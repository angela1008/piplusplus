# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20170411_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Membership')),
                ('group', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
            ],
        ),
    ]
