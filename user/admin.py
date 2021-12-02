from django.contrib import admin
from .models import Guest, Security, GuestType
# Register your models here.
admin.site.register(Guest)
admin.site.register(Security)
admin.site.register(GuestType)
