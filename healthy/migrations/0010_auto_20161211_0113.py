# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthy', '0009_auto_20161210_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=10),
        ),
    ]
