# Generated by Django 5.0.7 on 2024-07-22 09:15

import flights.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='cip_id',
            field=models.CharField(default=flights.models.generate_short_id, editable=False, max_length=4, unique=True),
        ),
    ]