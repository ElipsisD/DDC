# Generated by Django 4.2.1 on 2023-05-19 11:12

import django.core.validators
from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название')),
                ('coord', djgeojson.fields.PointField(verbose_name='координаты')),
                ('rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(25)], verbose_name='рейтинг')),
            ],
            options={
                'verbose_name': 'примечательное место',
                'verbose_name_plural': 'примечательные места',
            },
        ),
    ]
