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

    class Meta:
        verbose_name = 'BCT Property'
        verbose_name_plural = 'BCT Properties'

    def __str__(self):
        return self.bct_id


class BrewsterBorder(models.Model):
    fid = models.BigIntegerField(default=1)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name = 'Town of Brewster Border'
        verbose_name_plural = 'Town of Brewster Border'


class Narrative(models.Model):
    narrative = tinymce_models.HTMLField(default='intro narrative', blank=True)

    class Meta:
        verbose_name = 'Introduction Narrative'
        verbose_name_plural = 'Introduction Narrative'

    def __str__(self):
        return self.narrative
