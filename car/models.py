from django.db import models
from user.models import Guest
from django.utils.safestring import mark_safe

# Create your models here.
class Car(models.Model):
    def __str__(self):
        return self.name

    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name='car', null=False)
    name = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=20, null=True)
    license_plate = models.CharField(max_length=20, null=True, default='')
    color = models.CharField(max_length=20, null=True)
    car_registration = models.ImageField(upload_to='car-registrations',null=True)
    @property
    def thumbnail_registration(self):
        if self.car_registration:
            return mark_safe('<img src="{}" />'.format(self.car_registration.url))
        return ""
        
    image = models.ImageField(upload_to='cars',null=True)
    @property
    def thumbnail_image(self):
        if self.image:
            return mark_safe('<img src="{}" />'.format(self.image.url))
        return ""
    
    