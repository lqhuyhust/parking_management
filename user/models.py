from django.db import models
from django.contrib.auth.models import User
from car_park.models import Port, CarPark
from django.utils.safestring import mark_safe

# Create your models here.
class GuestType(models.Model):
    name = models.CharField(max_length=15, null=False)
    fee = models.DecimalField(max_digits=7, decimal_places= 7, default=0)
    
class Guest(User):
    class Meta:
        verbose_name = 'Guest'

    guest_type = models.ForeignKey(GuestType, on_delete=models.CASCADE, related_name="guest_type", default=1)
    expired_date = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    license = models.ImageField(upload_to='licenses', null=True)

    @property
    def thumbnail_license(self):
        if self.license:
            return mark_safe('<img src="{}" />'.format(self.license.url))
        return ""

class Security(User):
    class Meta:
        verbose_name = 'Staff'

    port = models.ForeignKey(Port, on_delete=models.DO_NOTHING, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False, default='')
