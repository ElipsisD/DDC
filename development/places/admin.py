from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ExportActionModelAdmin
from leaflet.admin import LeafletGeoAdminMixin

from places.models import Place, Weather


class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place


class PlaceAdmin(LeafletGeoAdminMixin, ImportExportActionModelAdmin):
    resource_class = PlaceResource
    list_display = ('name', 'get_coord')
    save_on_top = True

    def get_coord(self, object):
        return object.coord['coordinates']

    get_coord.short_description = 'координаты'


class WeatherResource(resources.ModelResource):
    class Meta:
        model = Weather


class WeatherAdmin(ExportActionModelAdmin):
    resource_class = WeatherResource
    readonly_fields = ('place', 'temperature', 'humidity', 'pressure',
                       'wind_direction', 'wind_speed', 'time_create')
    list_display = ('place', 'time_create')
    list_filter = ('place', 'time_create',)
    save_on_top = True


admin.site.register(Place, PlaceAdmin)
admin.site.register(Weather, WeatherAdmin)
