from rest_framework import generics, status
from rest_framework.response import Response
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
        target = (float(longitude), float(latitude))
    
        car_parks = CarPark.objects.all()
        serializer = CarParkSerializer(car_parks, many=True)
        for car_park in serializer.data:
            print((float(car_park['longitude']), float(car_park['latitude'])))
            coordinate = (float(car_park['longitude']) + ',' + float(car_park['latitude']))
            car_park['distance'] = geodesic(target,coordinate).km
        print(serializer.data)
        Response(serializer.data)     

class FollowCarPark(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            car_park = CarPark.objects.get(pk=pk)
        except CarPark.DoesNotExist:
            return Response('Car Park Not Found', status=status.HTTP_404_NOT_FOUND)
        num = car_park.available.count()

        data = {
            car_park: car_park.name, 
            message: "Update: Number of available parking slot is " + num
        }
        return Response(data, status=status.HTTP_200_OK)

