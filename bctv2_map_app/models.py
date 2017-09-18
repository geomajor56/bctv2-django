from django.contrib.gis.db import models
from tinymce import models as tinymce_models
from django.utils import timezone


class BctParcel(models.Model):
    bct_id = models.CharField(max_length=50)
    parcel_num = models.CharField(max_length=50, blank=True)
    owner_type = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=50, blank=True)
    acquired = models.DateField(blank=True, default='2017-10-10')
    grantor = models.CharField(max_length=100, blank=True)
    upland = models.FloatField(blank=True)
    wetland = models.FloatField(blank=True)
    habitat = models.CharField(max_length=50, blank=True)
    narrative = tinymce_models.HTMLField(default='type something here', blank=True)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.bct_id


class BrewsterBorder(models.Model):
    geom = models.PolygonField()


class Narrative(models.Model):
    narrative = tinymce_models.HTMLField(default='intro narrative', blank=True)

    def __str__(self):
        return self.narrative
