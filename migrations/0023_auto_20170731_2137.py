# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-31 21:37
# pylint: skip-file



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0022_auto_20170731_2133'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='datapoint',
            index_together=set([('source', 'generator_identifier', 'secondary_identifier'), ('generator_identifier', 'recorded'), ('source', 'generator_identifier'), ('generator_identifier', 'secondary_identifier', 'recorded'), ('source', 'created'), ('generator_identifier', 'secondary_identifier'), ('source', 'generator_identifier', 'secondary_identifier', 'recorded'), ('source', 'generator_identifier', 'secondary_identifier', 'created'), ('generator_identifier', 'created', 'recorded'), ('source', 'generator_identifier', 'created'), ('generator_identifier', 'secondary_identifier', 'created'), ('source', 'generator_identifier', 'created', 'recorded'), ('generator_identifier', 'created'), ('generator_identifier', 'secondary_identifier', 'created', 'recorded'), ('source', 'generator_identifier', 'secondary_identifier', 'created', 'recorded'), ('source', 'generator_identifier', 'recorded')]),
        ),
    ]
