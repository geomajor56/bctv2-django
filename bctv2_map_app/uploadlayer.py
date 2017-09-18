import os
from django.contrib.gis.utils import LayerMapping
from bctv2_map_app.models import BctParcel
import bctv2_map_app

bctparcel_mapping = {
    # 'gid': 'gid',
    'bct_id': 'BCT',
    'parcel_num': 'PID',
    'owner_type': 'OWNER_TYPE',
    'street_number': 'LOCNO',
    'street_name': 'STREET_NAM',
    'acquired': 'acdate',
    'grantor': 'GRANTOR',
    'upland': 'upfloat',
    'wetland': 'WETLAND',
    'habitat': 'HABITAT',
    'geom': 'MULTIPOLYGON',
}

parcel_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(bctv2_map_app.__file__), 'data', 'bctparcels.shp'))



def run(verbose=True):
    lmParcel = LayerMapping(BctParcel, parcel_mapping_shp, bctparcel_mapping, transform=False, encoding='iso-8859-1')
    lmParcel.save(strict=True, verbose=verbose)

