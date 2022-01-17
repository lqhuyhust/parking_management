from rest_framework import serializers
from .models import Parking

class ParkingSerializer(serializers.ModelSerializer):
    car_park = serializers.StringRelatedField()
    parking_slot = serializers.StringRelatedField()
    class Meta:
        model = Parking
        fields = ('id', 'car_park', 'parking_slot', 'time_start', 'time_end', 'fee', 'status', 'qr_code' )
