from rest_framework import generics
from .models import CarPark, ParkingSlot, Port
from .serializers import CarParkSerializer, CarParkSingleSerializer, ParkingSlotSerializer, ParkingSlotSingleSerializer, PortSerializer, PortSingleSerializer

# Create your views here.
class CarParkList(generics.ListCreateAPIView):
    queryset = CarPark.objects.all()
    serializer_class = CarParkSerializer

class CarParkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarPark.objects.all()
    serializer_class = CarParkSingleSerializer

class ParkingSlotList(generics.ListCreateAPIView):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer

class ParkingSlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSingleSerializer

class PortList(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

class PortDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSingleSerializer