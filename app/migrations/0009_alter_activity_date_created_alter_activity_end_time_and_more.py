# Generated by Django 4.0.4 on 2022-06-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_activity_end_time_activity_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]