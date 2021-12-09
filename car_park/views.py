from rest_framework import generics, status
from rest_framework.response import Response
from .models import CarPark, ParkingSlot, Port
from .serializers import CarParkSerializer, CarParkSingleSerializer, ParkingSlotSerializer, ParkingSlotSingleSerializer, PortSerializer, PortSingleSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from geopy.distance import geodesic
from parking.models import Parking, Payment
from parking.serializers import ParkingSerializer

# Create your views here.
class CarParkCreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = CarPark.objects.all()
    serializer_class = CarParkSerializer

class CarParkList(generics.ListAPIView):
    permission_classes = (AllowAny, )
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
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        longitude = self.request.query_params.get('long')
        latitude = self.request.query_params.get('lat')
        target = (float(longitude), float(latitude))
        car_parks = CarPark.objects.all()
        serializer = CarParkSerializer(car_parks, many=True)
        result = []
        for car_park in serializer.data:
            coordinate = (float(car_park['longitude']), float(car_park['latitude']))
            car_park['distance'] = geodesic(target,coordinate).km
            if car_park['distance'] < 3:
                result.append(car_park)
        return Response(result, status=status.HTTP_200_OK)     

class BookCarPark(APIView):
    def get_car_park(self, pk):
        try:
            return CarPark.objects.get(pk=pk)
        except CarPark.DoesNotExist:
            return Response('Car Park Not Found', status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        try:
            parking = Parking.objects.get(user_id=request.user.id, done=False)
        except Parking.DoesNotExist:
            pass
        else:
            return Response('You have to take only 1 car at same time', status=status.HTTP_400_BAD_REQUEST)

        pk = kwargs.get('pk')
        car_park = self.get_car_park(pk)

        data = {
            "user": request.user.id,
            "car": request.data['car'],
            "car_park": car_park.id,
            "estimate_end_time": request.data['estimate_end_time'],
            "fee": request.data['fee']
        }
        
        available = ParkingSlot.objects.filter(car_park_id=car_park.id, available=True)
        if len(available) == 0:
            return Response('There is no available parking slot!', status=status.HTTP_404_NOT_FOUND)
        else:
            data['parking_slot'] = available[0].id
        parking_serializer = ParkingSerializer(data=data)
        if parking_serializer.is_valid():
            parking_serializer.save()
            slot = Parking.objects.get(pk=available[0].id)
            slot.available = False
            slot.save()
            return Response(parking_serializer.data, status=status.HTTP_201_CREATED)
        return Response(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
