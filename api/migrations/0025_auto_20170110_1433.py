# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-10 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20170110_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='user_pic',
            field=models.ImageField(default='../static/media/user/default.png', upload_to='static/media/user/'),
        ),
    ]
