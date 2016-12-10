# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthy', '0007_auto_20161210_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markerpredefined',
            name='variant_type',
        ),
        migrations.AddField(
            model_name='marker',
            name='variant_type',
            field=models.CharField(choices=[('Gender', 'Gender'), ('Age', 'Age'), ('None', 'None')], default='None', max_length=10, verbose_name='Type'),
        ),
    ]