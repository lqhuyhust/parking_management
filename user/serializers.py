from rest_framework import serializers
from .models import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license', 'email', 'is_active', )

class GuestSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'username', 'first_name', 'last_name', 'license', 'email', 'expired_date', )
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}
