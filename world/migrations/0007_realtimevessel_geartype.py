# Generated by Django 3.0.8 on 2021-01-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_auto_20210130_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtimevessel',
            name='geartype',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
