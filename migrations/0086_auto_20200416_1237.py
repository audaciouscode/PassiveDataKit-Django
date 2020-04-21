# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-16 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0085_auto_20200327_1354'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='datapoint',
            index_together=set([('generator_definition', 'source_reference'), ('generator_definition', 'source_reference', 'created', 'recorded'), ('generator_definition', 'created'), ('generator_definition', 'source_reference', 'recorded'), ('generator_definition', 'source_reference', 'created'), ('source_reference', 'recorded'), ('source_reference', 'created')]),
        ),
    ]
