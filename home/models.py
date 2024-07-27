# home/models.py
from django.db import models
from django.contrib.auth.models import User


class TravelDestination(models.Model):
    object_id = models.PositiveIntegerField(primary_key=True)
    designation_num = models.CharField(max_length=20, verbose_name="Designation Number")
    county = models.CharField(max_length=100, verbose_name="County")
    prop_name = models.CharField(max_length=250, verbose_name="Property Name")
    phy_addr = models.CharField(max_length=500, verbose_name="Physical Address")
    city = models.CharField(max_length=250, verbose_name="City")
    zip_code = models.CharField(max_length=8, verbose_name="Zip")
    phone = models.CharField(max_length=16, verbose_name="Main Phone Number")
    web = models.URLField(max_length=250, verbose_name="Web Address")
    lodge_type = models.CharField(max_length=100, verbose_name="Type of Lodging Facility", null=True, blank=True)
    palm_level = models.CharField(max_length=10, verbose_name="Palm Level")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude", null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude", null=True, blank=True)
    image1 = models.URLField(max_length=2000, null=True, blank=True)
    image2 = models.URLField(max_length=2000, null=True, blank=True)
    image3 = models.URLField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.prop_name



class TravelDestinationDetails(models.Model):
    facility = models.ForeignKey(TravelDestination, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    price_range = models.CharField(max_length=100, null=True)
    eco_friendly_certifications = models.JSONField(null=True)
    available_activities = models.JSONField(null=True)
    amenities = models.JSONField(null=True)
    availability = models.CharField(max_length=255, null=True)
    special_offers = models.CharField(max_length=255, null=True)
    environmental_practices = models.CharField(max_length=255, null=True)
    conservation_projects = models.CharField(max_length=255, null=True)
    community_involvement = models.CharField(max_length=255, null=True)
    tags = models.JSONField(null=True)
    accessibility = models.CharField(max_length=255, null=True)
    pet_friendly = models.BooleanField(null=True)

    # def __str__(self):
    #     return f"EcoFriendlyHotel (Facility ID: {self.facilityid})"


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reviewed_facility = models.ForeignKey(TravelDestination, on_delete=models.CASCADE, null=True)

    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    name = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_title = models.CharField(max_length=255, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    date_of_visit = models.DateField()
    recommend = models.BooleanField(default=False)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name