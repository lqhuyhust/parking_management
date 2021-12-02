from django.contrib import admin
from .models import Parking, Payment
# Register your models here.
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'car_park', 'parking_slot', 'time_start', 'time_end', 'fee', 'extra_fee', 'done', )
    search_fields = ('user', )
    list_filter  = ('done','car_park', )
admin.site.register(Parking, ParkingAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car_park', 'parking_slot', 'type', 'fee', )
    search_fields = ('user', )
    list_filter  = ('car_park', )
admin.site.register(Payment, PaymentAdmin)