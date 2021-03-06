# pylint: skip-file
# Generated by Django 2.2.16 on 2020-09-18 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0090_auto_20200420_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='data_files', to='passive_data_kit.DataPoint'),
            preserve_default=False,
        ),
    ]
