from django.conf import settings
from django.db import models
from geocoding.utils import get_coordinates  # Assuming you have the geocoding utility

class BloodRequest(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    URGENCY_LEVELS = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group_needed = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    address = models.CharField(max_length=255, help_text="Enter the location for blood delivery or collection")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    urgency_level = models.IntegerField(choices=URGENCY_LEVELS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically geocode the address
        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = get_coordinates(self.address)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Request by {self.requester.username} for {self.blood_group_needed}"

    class Meta:
        ordering = ['-urgency_level', 'created_at']
