from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Profile  # only if Profile is in users app

admin.site.register(Profile)
