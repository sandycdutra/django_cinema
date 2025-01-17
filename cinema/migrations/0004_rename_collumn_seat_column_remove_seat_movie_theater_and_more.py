# Generated by Django 5.0.6 on 2024-07-12 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_movie_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='collumn',
            new_name='column',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='movie_theater',
        ),
        migrations.AddField(
            model_name='seat',
            name='session',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='cinema.session'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='status',
            field=models.CharField(choices=[('available', 'Disponível'), ('unavailable', 'Indisponível')], default='available', max_length=12),
        ),
    ]
