# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthy', '0005_auto_20161208_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='markerpredefined',
            name='variant',
            field=models.BooleanField(default=False, verbose_name='Variant'),
        ),
        migrations.AddField(
            model_name='markerpredefined',
            name='variant_age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='markerpredefined',
            name='variant_gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Child', 'Child'), ('N/A', 'N/A')], default='N/A', max_length=10, verbose_name='Gender'),
        ),
    ]
