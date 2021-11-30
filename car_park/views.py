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
        target = ("{:.6f}".format(float(longitude)), "{:.6f}".format(float(latitude)))
    
        car_parks = CarPark.objects.all()
        print('************')
        serializer = CarParkSerializer(car_parks, many=True)
        for car_park in serializer.data:
            print(("{:.6f}".format(float(car_park['longitude'])), "{:.6f}".format(float(car_park['latitude']))))
            coordinate = ("{:.6f}".format(float(car_park['longitude'])) + ',' + "{:.6f}".format(float(car_park['latitude'])))
            print('************')
            car_park['distance'] = geodesic(target,coordinate).km
        print(serializer.data)
        Response(serializer.data)      
