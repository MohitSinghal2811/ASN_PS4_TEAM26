# Generated by Django 3.0.8 on 2021-01-31 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0008_trajectory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trajectory',
            old_name='timestamp',
            new_name='times',
        ),
    ]