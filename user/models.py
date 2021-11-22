from django.db import models
from django.contrib.auth.models import User
from car_park.models import Port

ROLES = [
    ('Admin', 'Admin'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
]
# Create your models here.
class Guest(User):
    guest_type = models.ForeignKey(GuestType, on_delete=models.CASCADE, related_name="guest_type")
    license_plate = models.CharField(max_length=20, null=False)
    expired_date = models.DateField(null=False)
    date_of_birth = models.DateField(null=True)

class Security(User):
    port = models.ForeignKey(Port, on_delete=models.DO_NOTHING, null=False)

class GuestType(models.Model):
    name = models.CharField(max_length=15, null=False)
    fee = models.DecimalField(min=0)

class UserRole(models.Model):
    user = models.OneToOneField(User, related_name='role', on_delete=models.CASCADE, unique=True)
    role = models.CharField(choices=ROLES, default='Admin', max_length=20)