from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            from .utils import get_coordinates
            self.latitude, self.longitude = get_coordinates(self.address)
        super().save(*args, **kwargs)
