# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_userprofile_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='university_grad_date_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='university_grad_date_2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='university_grad_date_3',
        ),
    ]
