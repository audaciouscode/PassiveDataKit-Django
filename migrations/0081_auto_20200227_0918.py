# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-27 15:18


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0080_auto_20200221_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceissue',
            old_name='iu_related',
            new_name='ui_related',
        ),
    ]
