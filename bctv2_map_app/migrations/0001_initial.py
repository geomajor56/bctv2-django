# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 01:13
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BctParcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bct_id', models.CharField(max_length=50)),
                ('bct_poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='BctPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bct_id', models.CharField(max_length=50)),
                ('pid', models.CharField(blank=True, max_length=50)),
                ('owner_type', models.CharField(blank=True, max_length=50)),
                ('street_number', models.CharField(blank=True, max_length=10)),
                ('street_extension', models.CharField(blank=True, max_length=10)),
                ('acquired', models.DateField(blank=True)),
                ('grantor', models.CharField(blank=True, max_length=100)),
                ('upland', models.FloatField(blank=True)),
                ('wetland', models.FloatField(blank=True)),
                ('total', models.FloatField(blank=True)),
                ('narrative', tinymce.models.HTMLField(blank=True, default='type something here')),
                ('bct_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
