# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160427_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
