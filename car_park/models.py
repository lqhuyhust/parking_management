from django.db import models

# Create your models here.
class CarPark(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100, null=False)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False) 

    def __str__(self):
        return '%d' % (self.name)

class Port(models.Model):
    name = models.CharField(max_length=50, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)

class ParkingSlot(models.Model):
    name = models.CharField(max_length=50, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return '%d' % (self.name)
