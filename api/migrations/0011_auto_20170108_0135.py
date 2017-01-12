# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-07 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170108_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_pic',
            field=models.ImageField(default='media/Group/default.jpg', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='userextension',
            name='user_pic',
            field=models.ImageField(default='media/User/default.jpg', upload_to='media/'),
        ),
    ]
