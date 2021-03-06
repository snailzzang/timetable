# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name01',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name02',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name03',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name04',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name05',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name06',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name07',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name08',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name09',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name10',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat01',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat02',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat03',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat04',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat05',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat06',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat07',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat08',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat09',
        ),
        migrations.RemoveField(
            model_name='study',
            name='cat10',
        ),
        migrations.AddField(
            model_name='study',
            name='category',
            field=models.ManyToManyField(to='timeline.Category'),
        ),
    ]
