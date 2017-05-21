from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BctPoint, BctParcel

admin.site.register(BctPoint, LeafletGeoAdmin)
admin.site.register(BctParcel, LeafletGeoAdmin)