# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0067_auto_20190820_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceissue',
            name='platform_version',
        ),
    ]