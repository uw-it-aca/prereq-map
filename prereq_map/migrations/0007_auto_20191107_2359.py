# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

# Generated by Django 2.2.7 on 2019-11-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prereq_map', '0006_auto_20190425_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegraph',
            name='id',
        ),
        migrations.RemoveField(
            model_name='curricgraph',
            name='id',
        ),
        migrations.AlterField(
            model_name='coursegraph',
            name='course_id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curricgraph',
            name='curric_id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
