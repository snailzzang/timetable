# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_auto_20160701_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
