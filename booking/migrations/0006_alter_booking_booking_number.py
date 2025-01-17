# Generated by Django 5.0.4 on 2024-07-05 07:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking_booking_number_alter_booking_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
