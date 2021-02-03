# Generated by Django 3.0.8 on 2021-01-29 12:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anchorages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s2id', models.CharField(max_length=8)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Anchors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s2id', models.CharField(max_length=80)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('label', models.CharField(max_length=80)),
                ('sublabel', models.CharField(max_length=80, null=True)),
                ('label_sour', models.CharField(max_length=80)),
                ('iso3', models.CharField(max_length=80)),
                ('distance_f', models.CharField(max_length=80, null=True)),
                ('drift_radi', models.CharField(max_length=80, null=True)),
                ('at_dock', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='DriftingLonglines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mmsi', models.FloatField(null=True)),
                ('timestamp', models.FloatField(null=True)),
                ('distance_f', models.FloatField(null=True)),
                ('distance00', models.FloatField(null=True)),
                ('speed', models.FloatField(null=True)),
                ('course', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('is_fishing', models.FloatField(null=True)),
                ('source', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]