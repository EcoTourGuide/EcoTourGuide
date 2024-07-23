from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255, default="Unknown Site")
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} visited {self.site_name}"

class UnsplashImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    unsplash_image_id = models.CharField(max_length=255, unique=True)
    image_url = models.URLField(max_length=2000)

    def __str__(self):
        return f'{self.image_id} - {self.unsplash_image_id}'
