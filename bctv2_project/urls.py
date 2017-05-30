from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView

from bctv2_map_app.models import BctPoint, BctParcel, BrewsterBorder

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson.point$', GeoJSONLayerView.as_view(model=BctPoint), name='pointdata'),
    url(r'^data.geojson.parcel$', GeoJSONLayerView.as_view(model=BctParcel), name='parceldata'),
    url(r'^data.geojson.brewster$', GeoJSONLayerView.as_view(model=BrewsterBorder), name='brewsterdata'),
    url(r'^tinymce/', include('tinymce.urls')),

]
