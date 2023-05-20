from django.core.validators import MaxValueValidator
from django.db import models
from djgeojson.fields import PointField


class Place(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    coord = PointField()
    rate = models.PositiveSmallIntegerField(verbose_name='рейтинг', validators=[MaxValueValidator(25)], default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'примечательное место'
        verbose_name_plural = 'примечательные места'


class Weather(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='примечательное место')
    temperature = models.SmallIntegerField(verbose_name='температура, С')
    humidity = models.PositiveSmallIntegerField(verbose_name='влажность воздуха, %', validators=[MaxValueValidator(100)])
    pressure = models.PositiveSmallIntegerField(verbose_name='атмосферное давление, мм рт. ст.')
    wind_direction = models.CharField(verbose_name='направление ветра')
    wind_speed = models.SmallIntegerField(verbose_name='скорость ветра, м/с')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата запроса')

    def __str__(self):
        # return f'{self.pk}: Погода в {self.place.name} {self.time_create}'
        return f'{self.pk}: Погода в {self.place.name}'

    class Meta:
        verbose_name = 'показание погоды'
        verbose_name_plural = 'показания погоды'
