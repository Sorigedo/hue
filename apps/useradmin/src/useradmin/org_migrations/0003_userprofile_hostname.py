# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0002_auto_20200130_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hostname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
