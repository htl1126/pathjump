# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20160505_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='university_grad_date_1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='university_grad_date_2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='university_grad_date_3',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
