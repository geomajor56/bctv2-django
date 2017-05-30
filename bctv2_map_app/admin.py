from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BctPoint, BctParcel, BrewsterBorder, Narrative

admin.site.register(BctPoint, LeafletGeoAdmin)
admin.site.register(BctParcel, LeafletGeoAdmin)
admin.site.register(BrewsterBorder, LeafletGeoAdmin)
admin.site.register(Narrative, LeafletGeoAdmin)
