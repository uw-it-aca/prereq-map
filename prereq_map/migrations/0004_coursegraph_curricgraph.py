# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

# Generated by Django 2.1.7 on 2019-04-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prereq_map', '0003_auto_20190306_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=12)),
                ('graph_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CurricGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curric_id', models.CharField(max_length=12)),
                ('graph_data', models.TextField()),
            ],
        ),
    ]
