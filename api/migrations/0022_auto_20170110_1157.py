# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-10 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20170110_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_pic',
            field=models.ImageField(default='/static/media/group/default.png', upload_to='static/media/group/'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='user_pic',
            field=models.ImageField(default='/static/media/group/default.png', upload_to='static/media/user/'),
        ),
    ]
