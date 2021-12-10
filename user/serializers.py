from rest_framework import serializers

import car_park
from .models import Guest, GuestType, Security

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license', 'email', 'is_active', )

class GuestSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license', 'email', 'expired_date', )
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'car_park', 'port')

class SecuritySingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'car_park', 'port' )
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}
    
    car_park = serializers.StringRelatedField(required=False)
    port = serializers.StringRelatedField(required=False)

class GuestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestType
        fields = ('name', 'fee', )