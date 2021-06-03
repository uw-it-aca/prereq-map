# Generated by Django 2.2.22 on 2021-05-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prereq_map', '0007_auto_20191107_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGraphCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=12, unique=True)),
                ('needs_rebuild', models.BooleanField(default=False)),
                ('graph_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CurricGraphCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curric_id', models.CharField(max_length=12, unique=True)),
                ('needs_rebuild', models.BooleanField(default=False)),
                ('graph_data', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CourseGraph',
        ),
        migrations.DeleteModel(
            name='CurricGraph',
        ),
    ]
