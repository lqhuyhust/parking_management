from rest_framework import serializers
from .models import CarPark, ParkingSlot, Port

class CarParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('name', 'location', 'longitude', 'latitude', )

class CarParkSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('name', 'location', 'longitude', 'latitude', )
    
    name = serializers.CharField(max_length=50, required=False)
    location = serializers.CharField(max_length=100, required=False)
    longitude = serializers.FloatField(required=False)
    latitude = serializers.FloatField(required=False)
    
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('name', 'car_park', 'available', )

class ParkingSlotSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('name', 'car_park', 'available', )
        extra_kwargs = {'car_park': {'read_only': True}}
    
    name = serializers.CharField(max_length=50,  required=False)
    available = serializers.BooleanField(required=False)

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('name', 'car_park', )

class PortSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('name', 'car_park', )
        extra_kwargs = {'car_park': {'read_only': True}}