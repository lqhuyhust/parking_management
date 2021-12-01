from django.db import models
from user.models import Guest
from car_park.models import CarPark, ParkingSlot 
# Create your models here.
PAYMENT_TYPES = [
    ('Booking', 'Booking'),
    ('Extra', 'Extra')
]
class Parking(models.Model):
    user = models.ForeignKey(Guest, on_delete=models.CASCADE, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, null=False)
    estimate_end_time = models.DateTimeField(null=True)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
    extra_fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
    is_paid = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

class Payment(models.Model):
    user = models.ForeignKey(Guest, on_delete=models.CASCADE, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, null=False)
    type = models.CharField(choices=PAYMENT_TYPES, default='Booking', max_length=10)
    fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
