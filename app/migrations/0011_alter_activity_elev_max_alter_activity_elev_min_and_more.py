# Generated by Django 4.0.4 on 2022-06-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_activity_elev_max_activity_elev_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='elev_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activity',
            name='elev_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activity',
            name='heartrate_avg',
            field=models.IntegerField(default=0),
        ),
    ]