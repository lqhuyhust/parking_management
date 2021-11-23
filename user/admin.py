from django.contrib import admin
from .models import Guest, Security, UserRole, GuestType
# Register your models here.
admin.site.register(Guest)
admin.site.register(Security)
admin.site.register(UserRole)
admin.site.register(GuestType)
