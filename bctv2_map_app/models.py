from django.contrib.gis.db import models
from tinymce import models as tinymce_models


class BctPoint(models.Model):
    bct_id = models.CharField(max_length=50)
    pid = models.CharField(max_length=50, blank=True)
    owner_type = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    street_extension = models.CharField(max_length=10, blank=True)
    acquired = models.DateField(blank=True)
    grantor = models.CharField(max_length=100, blank=True)
    upland = models.FloatField( blank=True)
    wetland = models.FloatField( blank=True)
    total = models.FloatField( blank=True)
    narrative = tinymce_models.HTMLField(default='type something here', blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.bct_id
 

class BctParcel(models.Model):
    bct_id = models.CharField(max_length=50)
    geom = models.PolygonField()

    def __str__(self):
        return self.bct_id


class BrewsterBorder(models.Model):
    geom = models.PolygonField()


class Narrative(models.Model):
    narrative = tinymce_models.HTMLField(default='intro narrative', blank=True)

    def __str__(self):
        return self.narrative
