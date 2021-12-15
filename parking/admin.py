from django.contrib import admin
from .models import Parking
# Register your models here.
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'car_park', 'parking_slot', 'time_start', 'time_end', 'status' )
    search_fields = ('user', )
    list_filter  = ('status','car_park', )
admin.site.register(Parking, ParkingAdmin)
