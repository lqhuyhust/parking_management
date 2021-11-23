from rest_framework import serializers

import car_park
from .models import Guest, GuestType, Security, UserRole

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license_plate', 'email', )

class GuestSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license_plate', 'email', )
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}

    license_plate = serializers.CharField(required=False)
    expired_date = serializers.DateField(required=False)

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

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('user', 'role', )

class GuestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestType
        fields = ('name', 'fee', )