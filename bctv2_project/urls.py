from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView

from bctv2_map_app.models import BctPoint

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=BctPoint), name='data'),
    url(r'^tinymce/', include('tinymce.urls')),

]
