from django.db import models

# Create your models here.
class CarPark(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100, null=False)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return self.name

    @property
    def available(self):
        result = []
        for slot in ParkingSlot.objects.filter(car_park_id=self.id):
            result.append(slot.name)
        return result
    
    @property
    def available_number(self):
        return len(self.available)
        
class ParkingSlot(models.Model):
    slot_id = models.CharField(max_length=5, default='')
    name = models.CharField(max_length=50, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
