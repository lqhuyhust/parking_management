from django.contrib import admin
from .models import CarPark, ParkingSlot, Port
# Register your models here.

class CarParkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'available_number', )
    readonly_fields = ('available',)
    search_fields = ('name', )
admin.site.register(CarPark, CarParkAdmin)

class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'slot_id', 'name', 'car_park', 'available', )
    list_filter  = ('car_park', )
    search_fields = ('name', )
admin.site.register(ParkingSlot, ParkingSlotAdmin)

class PortSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_park', )
    list_filter  = ('car_park', )
    search_fields = ('name', )
admin.site.register(Port, PortSlotAdmin)
