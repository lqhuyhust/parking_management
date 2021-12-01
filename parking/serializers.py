from rest_framework import serializers
from .models import Parking, Payment

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('user', 'car_park', 'parking_slot', 'time_start', 'time_end', 'fee', 'extra_fee', )

class ParkingSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('user', 'car_park', 'parking_slot', 'time_start', 'time_end', 'fee', 'extra_fee', )
        extra_kwargs = {'user': {'read_only': True}}
    
    car_park = serializers.StringRelatedField(required=False)
    parking_slot = serializers.StringRelatedField(required=False)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'car_park', 'parking_slot', 'type', 'fee', )