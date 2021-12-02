from django.db import models
from user.models import Guest

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)
    car_registration = models.CharField(max_length=20, null=False)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='car', null=False)

    def __str__(self):
        return self.name
