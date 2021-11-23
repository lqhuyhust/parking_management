from rest_framework import generics

from car_park import serializers
from .models import Parking
from .serializers import ParkingSerializer, ParkingSingleSerializer

# Create your views here.
class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


class ParkingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer