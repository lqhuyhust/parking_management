from django.db import models
from django.contrib.auth.models import User
from car_park.models import Port, CarPark

# Create your models here.
class GuestType(models.Model):
    name = models.CharField(max_length=15, null=False)
    fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
    
class Guest(User):
    guest_type = models.ForeignKey(GuestType, on_delete=models.CASCADE, related_name="guest_type")
    license_plate = models.CharField(max_length=20, null=False)
    expired_date = models.DateField(null=False)
    date_of_birth = models.DateField(null=True)

class Security(User):
    port = models.ForeignKey(Port, on_delete=models.DO_NOTHING, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False, default='')
