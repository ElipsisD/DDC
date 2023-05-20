import os

from pyowm import OWM
from pyowm.utils.config import get_default_config

from places.models import Place, Weather


def get_weather() -> None:
    """Обращается к API, получает данные о погоде всех мест и сохраняет в базе"""
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM(os.environ.get('WEATHER_API'), config_dict)
    weather_manager = owm.weather_manager()
    queryset = Place.objects.all()
    weather_data = []
    for place in queryset:
        coord = place.coord['coordinates']
        lon, lat = coord
        weather = weather_manager.weather_at_coords(lat,lon).weather
        weather_data.append(Weather(
            place=place,
            temperature=round(weather.temperature('celsius')['temp']),
            humidity=round(weather.humidity),
            pressure=round(weather.barometric_pressure('inHg')['press'] * 25.4),
            wind_direction=round(weather.wind().get('deg', 0)),
            wind_speed=round(weather.wind().get('speed', 0)),
        ))
    Weather.objects.bulk_create(weather_data)
