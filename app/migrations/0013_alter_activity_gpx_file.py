# Generated by Django 4.0.6 on 2022-10-03 11:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_activity_gpx_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='gpx_file',
            field=cloudinary.models.CloudinaryField(blank=True, default='manual', max_length=255, verbose_name=''),
        ),
    ]
