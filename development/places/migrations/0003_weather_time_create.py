# Generated by Django 4.2.1 on 2023-05-20 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_coord_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата запроса'),
            preserve_default=False,
        ),
    ]
