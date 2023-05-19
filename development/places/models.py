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
