# Generated by Django 3.0.8 on 2021-02-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0015_anomaly_col0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anomaly',
            name='cargo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='length',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='status',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='vesseltype',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='width',
            field=models.FloatField(null=True),
        ),
    ]