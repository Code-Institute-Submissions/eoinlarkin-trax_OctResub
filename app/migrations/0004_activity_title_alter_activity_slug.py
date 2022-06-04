# Generated by Django 4.0.4 on 2022-06-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_activity_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='title',
            field=models.CharField(default='Trax Activity', max_length=25),
        ),
        migrations.AlterField(
            model_name='activity',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
