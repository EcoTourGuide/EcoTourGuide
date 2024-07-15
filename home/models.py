# home/models.py
from django.db import models


class TravelDestination(models.Model):
    object_id = models.AutoField(primary_key=True)
    designation_num = models.CharField(max_length=20, verbose_name="Designation Number")
    county = models.CharField(max_length=100, verbose_name="County")
    prop_name = models.CharField(max_length=250, verbose_name="Property Name")
    phy_addr = models.CharField(max_length=500, verbose_name="Physical Address")
    city = models.CharField(max_length=250, verbose_name="City")
    zip_code = models.CharField(max_length=8, verbose_name="Zip")
    phone = models.CharField(max_length=16, verbose_name="Main Phone Number")
    web = models.URLField(max_length=250, verbose_name="Web Address")
    lodge_type = models.CharField(max_length=100, verbose_name="Type of Lodging Facility")
    palm_level = models.CharField(max_length=10, verbose_name="Palm Level")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")

    def __str__(self):
        return self.prop_name
