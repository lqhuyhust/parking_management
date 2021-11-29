from rest_framework import generics
from rest_framework.response import Response

import car_park
from .models import CarPark, ParkingSlot, Port
from .serializers import CarParkSerializer, CarParkSingleSerializer, ParkingSlotSerializer, ParkingSlotSingleSerializer, PortSerializer, PortSingleSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from geopy.distance import geodesic

# Create your views here.
class CarParkList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = CarPark.objects.all()
    serializer_class = CarParkSerializer

class CarParkDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = CarPark.objects.all()
    serializer_class = CarParkSingleSerializer

class ParkingSlotList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer

class ParkingSlotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSingleSerializer

class PortList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Port.objects.all()
    serializer_class = PortSerializer

class PortDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Port.objects.all()
    serializer_class = PortSingleSerializer

class SearchCarPark(APIView):
    def get(self, request, *args, **kwargs):
        longitude = kwargs.get('long')
        latitude = kwargs.get('lat')

        data = []
        you = ("73.6490763,-43.9762069")

        me = ("73.646628,-43.970497")

        print(geodesic(me,you).km)
        car_parks = CarPark.objects.all()
        Response(longitude)      
