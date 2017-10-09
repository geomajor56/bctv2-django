from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BctParcel, BrewsterBorder, Narrative


class BctParcelAdmin(LeafletGeoAdmin):
    fields = (('bct_id', 'grantor', 'acquired', 'narrative'), 'geom')
    list_display = ('bct_id', 'grantor', 'acquired', 'habitat', 'upland', 'wetland')
    date_hierarchy = 'acquired'
    settings_overrides = {
        'SPATIAL_EXTENT': (-69.95904922485353, 41.777072623006156, -70.17877578735353, 41.7177741935448),
        'DEFAULT_CENTER': (41.79895948813606, -70.3070068359375),
        'DEFAULT_ZOOM': 13,
        'MIN_ZOOM': 10,
        'MAX_ZOOM': 18,
        'TILES': [('OSM', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                   '© <a href="http://www.openstreetmap.org/copyright" target="_blank"> OpenStreetMap</a> contributors'),
                  ],
    }

    class BrewsterBorderAdmin(LeafletGeoAdmin):

        settings_overrides = {
            'SPATIAL_EXTENT': (-69.95904922485353, 41.777072623006156, -70.17877578735353, 41.7177741935448),
            'DEFAULT_CENTER': (41.79895948813606, -70.3070068359375),
            'DEFAULT_ZOOM': 13,
            'MIN_ZOOM': 10,
            'MAX_ZOOM': 18,
            'TILES': [('OSM', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                       '© <a href="http://www.openstreetmap.org/copyright" target="_blank"> OpenStreetMap</a> contributors'),
                      ],
        }


admin.site.register(BctParcel, BctParcelAdmin)
admin.site.register(BrewsterBorder, LeafletGeoAdmin)
admin.site.register(Narrative, LeafletGeoAdmin)
