from rest_framework import serializers
from .models import CarPark, ParkingSlot

class CarParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('id', 'name', 'location', 'longitude', 'latitude', 'available_number')
    
    available_number = serializers.SerializerMethodField()

    def get_available_number(self, obj):
        return len(ParkingSlot.objects.filter(car_park=obj, available=True))

class CarParkSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPark
        fields = ('name', 'location', 'longitude', 'latitude', 'available_number')
    
    name = serializers.CharField(max_length=50, required=False)
    location = serializers.CharField(max_length=100, required=False)
    longitude = serializers.FloatField(required=False)
    latitude = serializers.FloatField(required=False)
    available_number = serializers.SerializerMethodField()

    def get_available_number(self, obj):
        return len(ParkingSlot.objects.filter(car_park=obj, available=True))

    
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('name', 'car_park', 'available', )
