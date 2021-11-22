from rest_framework import serializers
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
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )

class SecuritySingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('user', 'role', )

class GuestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestType
        fields = ('name', 'fee', )