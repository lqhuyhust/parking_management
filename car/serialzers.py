from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'name', 'color', 'car_registration', 'guest', 'license_plate', 'image')

class CarSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'name', 'color', 'car_registration', 'guest', 'license_plate', 'image')
    
    brand = serializers.CharField(max_length=20, required=False)
    name = serializers.CharField(max_length=20, required=False)
    color = serializers.CharField(max_length=20, required=False)
    car_registration = serializers.CharField(max_length=20, required=False)
    guest = serializers.StringRelatedField(required=False)
    