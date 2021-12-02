from django.contrib.auth.models import Permission
from django.contrib import admin

# Register your models here.
admin.site.site_header = 'Parking Management'
admin.site.register(Permission)
