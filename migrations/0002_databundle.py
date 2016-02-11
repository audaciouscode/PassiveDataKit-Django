# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 01:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded', models.DateTimeField()),
                ('properties', django.contrib.postgres.fields.jsonb.JSONField()),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
