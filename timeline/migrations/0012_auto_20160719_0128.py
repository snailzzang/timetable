# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_auto_20160711_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='timeline'),
        ),
    ]