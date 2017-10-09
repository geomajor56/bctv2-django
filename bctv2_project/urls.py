from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
from django.utils.translation import ugettext_lazy as _
from bctv2_map_app.models import BctParcel, BrewsterBorder
from baton.autodiscover import admin
# from bctv2_map_app.views import MyModal

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson.parcel$', GeoJSONLayerView.as_view(model=BctParcel, properties=('bct_id',
                                                                                        'parcel_num',
                                                                                        'owner_type',
                                                                                        'street_number',
                                                                                        'street_name',
                                                                                        'acquired',
                                                                                        'grantor',
                                                                                        'upland',
                                                                                        'wetland',
                                                                                        'habitat',
                                                                                        'narrative')), name='parceldata'),
    url(r'^data.geojson.brewster$', GeoJSONLayerView.as_view(model=BrewsterBorder), name='brewsterdata'),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^mymodal/', MyModal.as_view(), name='mymodal'),

]

admin.site.site_header = _("Brewster Conservation Trust")
admin.site.site_title = _("My Site Admin")
