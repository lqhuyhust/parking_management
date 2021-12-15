from rest_framework import serializers
from .models import Parking

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'car_park', 'parking_slot', 'time_start', 'time_end', 'status' )
