from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BloodRequest  # only if these are in donations


admin.site.register(BloodRequest)
