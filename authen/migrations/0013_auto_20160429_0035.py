# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 00:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0012_auto_20160424_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 0, 35, 33, 529427, tzinfo=utc)),
        ),
    ]
