import os
from django.contrib.gis.utils import LayerMapping
from bctv2_map_app.models import BctPoint, BctParcel


point_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bctv2_map_app/data/points.shp'))
parcel_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bctv2_map_app/data/parcels.shp'))

point_mapping = {

    'bct_id': 'BCT',
    'pid': 'PID',
    'owner_type': 'OWNER_TYPE',
    'street_number': 'LOCNO',
    'street_extension': 'LOCEXT',
    'acquired': 'ACQUIRED',
    'grantor': 'GRANTOR',
    'upland': 'UPLAND',
    'wetland': 'WETLAND',
    'narrative': 'NARRATIVE',
    'geom': 'geom'
}

parcel_mapping = {
    'bct_id': 'BCT',
    'pid': 'PID',
    'geom': 'geom'
}


def run(verbose=True):
    lmPoint = LayerMapping(BctPoint, point_mapping_shp, point_mapping,
                           transform=False, encoding='iso-8859-1')
    lmPoint.save(strict=True, verbose=verbose)

    lmParcel = LayerMapping(BctParcel, parcel_mapping_shp, parcel_mapping_shp,
                            transform=False, encoding='iso-8859-1')
    lmParcel.save(strict=True, verbose=verbose)
