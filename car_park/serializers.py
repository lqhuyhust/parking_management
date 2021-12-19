from rest_framework import serializers
from .models import CarPark, ParkingSlot

class CarParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('id', 'name', 'location', 'longitude', 'latitude', 'available_number')

class CarParkSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('name', 'location', 'longitude', 'latitude', 'available_number')
    
    name = serializers.CharField(max_length=50, required=False)
    location = serializers.CharField(max_length=100, required=False)
    longitude = serializers.FloatField(required=False)
    latitude = serializers.FloatField(required=False)
    
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('name', 'car_park', 'available', )
