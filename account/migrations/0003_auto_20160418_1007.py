# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160417_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='university',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]