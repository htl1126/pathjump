# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('industry', models.CharField(blank=True, max_length=50)),
                ('employment_type', models.CharField(blank=True, max_length=50)),
                ('experience', models.CharField(blank=True, max_length=50)),
                ('job_function', models.CharField(blank=True, max_length=50)),
                ('company_logo', models.ImageField(upload_to='company_logo')),
            ],
        ),
    ]