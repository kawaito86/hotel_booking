# Generated by Django 5.0.4 on 2024-07-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_room_descriptions_alter_booking_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='coverimage_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='image_url2',
            field=models.URLField(blank=True),
        ),
    ]