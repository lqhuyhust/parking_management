from django.contrib import admin
from .models import CarPark, ParkingSlot, Port
# Register your models here.
admin.site.register(CarPark)
admin.site.register(ParkingSlot)
admin.site.register(Port)
