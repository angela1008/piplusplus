# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-09 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20170109_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextension',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_pic',
            field=models.ImageField(default='/media/group/default.png', upload_to='/media/group/'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='user_pic',
            field=models.ImageField(blank=True, default='media/User/default.jpg', null=True, upload_to='media/'),
        ),
    ]
