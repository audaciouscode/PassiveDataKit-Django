# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-21 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0089_merge_20200420_2124'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='datapoint',
            index_together=set([]),
        ),
    ]