# Generated by Django 3.0.8 on 2021-02-01 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0016_auto_20210202_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anomaly',
            old_name='basedateti',
            new_name='datetime',
        ),
    ]