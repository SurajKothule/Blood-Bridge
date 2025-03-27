from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)  # Required by Django
    phone_number = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Username is still required but not used for login

    def __str__(self):
        return self.email


class Profile(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    address = models.CharField(max_length=255, help_text="Enter your full address")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_donor = models.BooleanField(default=False)
    availability = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True, help_text="Date of last blood donation")

    def __str__(self):
        return f"{self.user.username} - {self.blood_group}"

    def save(self, *args, **kwargs):
        # Automatically convert address to latitude/longitude
        if not self.latitude or not self.longitude:
            from geocoding.utils import get_coordinates  # Assuming geocoding utility exists
            self.latitude, self.longitude = get_coordinates(self.address)
        super().save(*args, **kwargs)
