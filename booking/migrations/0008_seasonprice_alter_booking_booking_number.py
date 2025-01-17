# Generated by Django 5.0.4 on 2024-07-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_booking_booking_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('markup_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Markup Percentage')),
                ('markdown_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Markdown Percentage')),
            ],
            options={
                'verbose_name': 'Season Price',
                'verbose_name_plural': 'Season Prices',
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='9e154ce2-8f4', max_length=12, unique=True),
        ),
    ]
