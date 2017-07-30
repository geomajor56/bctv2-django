__author__ = 'michael'
import os
from django.contrib.gis.utils import LayerMapping
from bctv2_map_app.models import BctPoint, BctParcel

point_mapping = {
    'bct_id': 'sta_num',
    'station_name': 'StationNam',
    'station_alt_name': 'StationID',
    'geom': 'POINT'
}

parcel_mapping = {

}

point_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bctv2_map_app/data/points.shp'))
parcel_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bctv2_map_app/data/parcels.shp'))

def run(verbose=True):
    lm = LayerMapping(MonitorStation, station_shp, point_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)