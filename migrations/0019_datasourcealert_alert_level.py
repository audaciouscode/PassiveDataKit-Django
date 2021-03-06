# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 14:56
# pylint: skip-file



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0018_datasourcealert_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasourcealert',
            name='alert_level',
            field=models.CharField(choices=[('info', 'Informative'), ('warning', 'Warning'), ('critical', 'Critical')], default='info', max_length=64),
        ),
    ]
