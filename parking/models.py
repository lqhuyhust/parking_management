from django.db import models
from user.models import Guest
from car_park.models import CarPark, ParkingSlot 
import qrcode
import uuid
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

STATUS = [
    ('Pending', 'Pending'),
    ('Booked', 'Booked'),
    ('Completed', 'Completed')
]
class Parking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Guest, related_name='parking', on_delete=models.CASCADE, null=False)
    car_park = models.ForeignKey(CarPark, on_delete=models.CASCADE, null=False)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, null=False)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    fee = models.IntegerField(default=0)
    qr_code = models.ImageField(blank=True, upload_to='qrcode')
    status = models.CharField(choices=STATUS, max_length=10, default='Pending')

    