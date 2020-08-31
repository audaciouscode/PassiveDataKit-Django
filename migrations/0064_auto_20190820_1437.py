# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 19:37


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0063_auto_20190806_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, max_length=1048576, null=True)),
                ('platform_version', models.CharField(blank=True, max_length=1048576, null=True)),
                ('notes', models.TextField(blank=True, max_length=1048576, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('opened', 'Opened'), ('in-progress', 'In Progress'), ('resolved', 'Resolved'), ('wont-fix', "Won't Fix")], max_length=1024)),
                ('created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('description', models.TextField(blank=True, max_length=1048576, null=True)),
                ('stability_related', models.BooleanField(default=False)),
                ('uptime_related', models.BooleanField(default=False)),
                ('responsiveness_related', models.BooleanField(default=False)),
                ('battery_use_related', models.BooleanField(default=False)),
                ('power_management_related', models.BooleanField(default=False)),
                ('data_volume_related', models.BooleanField(default=False)),
                ('data_quality_related', models.BooleanField(default=False)),
                ('bandwidth_related', models.BooleanField(default=False)),
                ('storage_related', models.BooleanField(default=False)),
                ('configuration_related', models.BooleanField(default=False)),
                ('location_related', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='passive_data_kit.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=1024)),
                ('manufacturer', models.CharField(max_length=1024)),
                ('notes', models.TextField(blank=True, max_length=1048576, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='passive_data_kit.DeviceModel'),
        ),
        migrations.AddField(
            model_name='device',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='passive_data_kit.DataSource'),
        ),
    ]
