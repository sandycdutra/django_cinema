# Generated by Django 5.0.6 on 2024-07-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_movietheater_seat_session_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='release_year'),
        ),
    ]
