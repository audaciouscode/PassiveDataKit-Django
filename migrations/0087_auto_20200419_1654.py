# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-19 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0086_auto_20200416_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='secondary_identifier',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]