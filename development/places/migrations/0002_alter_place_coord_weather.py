# Generated by Django 4.2.1 on 2023-05-20 04:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coord',
            field=djgeojson.fields.PointField(),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.SmallIntegerField(verbose_name='температура, С')),
                ('humidity', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='влажность воздуха, %')),
                ('pressure', models.PositiveSmallIntegerField(verbose_name='атмосферное давление, мм рт. ст.')),
                ('wind_direction', models.CharField(verbose_name='направление ветра')),
                ('wind_speed', models.SmallIntegerField(verbose_name='скорость ветра, м/с')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='примечательное место')),
            ],
            options={
                'verbose_name': 'показание погоды',
                'verbose_name_plural': 'показания погоды',
            },
        ),
    ]
