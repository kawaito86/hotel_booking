# Generated by Django 5.0.4 on 2024-07-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_seasonprice_alter_booking_booking_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('markup_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('markdown_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('is_high_season', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='SeasonPrice',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='e345d046-56d', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]