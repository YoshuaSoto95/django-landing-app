# Generated by Django 5.1.7 on 2025-03-25 12:09

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='location',
            field=models.CharField(default=dashboard.models.get_location, max_length=100),
        ),
    ]
