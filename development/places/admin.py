from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin
from leaflet.admin import LeafletGeoAdminMixin
from places.models import Place


class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place

    # def dehydrate_coord(self, place):
    #     coord = getattr(place, 'coord', 'unknown')
    #     return coord['type']


class PlaceAdmin(LeafletGeoAdminMixin, ImportExportActionModelAdmin):
    resource_class = PlaceResource
    list_display = ('name', 'coord')


admin.site.register(Place, PlaceAdmin)
