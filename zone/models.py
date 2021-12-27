from django.db import models
from django.db.models.fields import CharField

FLOOR_NUMBER = (
    (1, 1),
    (2, 2)
)
# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=10, null=False)
    floor = models.IntegerField(choices=FLOOR_NUMBER, default=1)
    data = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    def __str__(self):
        floor = str(self.floor)
        return f'F{floor}-{self.name}'