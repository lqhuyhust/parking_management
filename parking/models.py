from django.db import models
from user.models import Guest
from car_park.models import CarPark, ParkingSlot 
from car.models import Car
# Create your models here.

STATUS = [
    ('Pending', 'Pending'),
    ('Booked', 'Booked'),
    ('Completed', 'Completed')
]
class Parking(models.Model):
    user = models.ForeignKey(Guest, related_name='parking', on_delete=models.CASCADE, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, null=False)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
    status = models.CharField(choices=STATUS, max_length=10, default='Pending')
