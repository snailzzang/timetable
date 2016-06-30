# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 09:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timeline', '0005_audience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audience',
            name='members',
        ),
        migrations.AddField(
            model_name='audience',
            name='audience',
            field=models.ManyToManyField(related_name='audience', to=settings.AUTH_USER_MODEL),
        ),
    ]
