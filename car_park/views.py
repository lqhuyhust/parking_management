from rest_framework import generics, status
from rest_framework import response
from rest_framework.response import Response
from user.models import Guest
from .models import CarPark, ParkingSlot
from .serializers import CarParkSerializer, CarParkSingleSerializer, ParkingSlotSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from geopy.distance import geodesic
from parking.models import Parking
from django.db import transaction

from django_q.models import Schedule
import requests
import json
API_URL = 'http://localhost:9000/api/zones/'
CAR_PARK_ID = 1
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
    permission_classes = (AllowAny, )
    queryset = CarPark.objects.all()
    serializer_class = CarParkSingleSerializer

class ParkingSlotList(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer

    def get(self, request, *args, **kwargs):
        car_park_id = kwargs.get('car_park_id')
        try:
            parking_slots = ParkingSlot.objects.filter(car_park_id=car_park_id)
        except ParkingSlot.DoesNotExist:
            return Response('Not Found', status=status.HTTP_404_NOT_FOUND)
        serializer = ParkingSlotSerializer(parking_slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  


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
            if car_park['distance'] < 2:
                result.append(car_park)
        return Response(result, status=status.HTTP_200_OK)     

class BookCarPark(APIView):
    # permission_classes = (AllowAny, )
    def get_car_park(self, pk):
        try:
            return CarPark.objects.get(pk=pk)
        except CarPark.DoesNotExist:
            return Response({'status': 404, 'message':'Car Park Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        if Parking.objects.filter(user_id=request.user.id, status__in=['Pending', 'Booked']):
            return Response({'status': 400, 'message':'You have to book only 1 car park at same time'}, status=status.HTTP_400_BAD_REQUEST)
        pk = kwargs.get('pk')
        
        available = ParkingSlot.objects.filter(car_park_id=pk, available=True).first()
        if not available:
            return Response({'status': 404, 'message':'There is no available parking slot!'}, status=status.HTTP_404_NOT_FOUND)
            
        new_parking = Parking(user=Guest.objects.get(pk=request.user.id), car_park=self.get_car_park(pk), parking_slot=available)
        new_parking.save()

        data = {
            "user": request.user.username,
            "car_park": self.get_car_park(pk).name,
            "parking_slot": available.name
        }

        response = {
            'status': 201,
            'data': data
        }

        available.available = False
        available.save()
        return Response(response, status=status.HTTP_201_CREATED)

def get_data():
    car_park = CarPark.objects.get(id=CAR_PARK_ID)
    response_API = requests.get(API_URL)
    available_slots = []
    data = json.loads(response_API.text)
    for zone in data:
        zone['data'] = bin(zone['data'])[2:].zfill(zone['number'])
        i = 1
        with transaction.atomic():
            for val in zone['data']:
                floor = zone['floor']
                name = zone['name']
                name = f'F{floor}-{name}-{i}'
                if(val == '0'):
                    available = False
                if(val == '1'):
                    available = True
                ParkingSlot.objects.filter(name=name, car_park=car_park).update(available=available)
                
                i = i + 1
    print(data)


Schedule.objects.create(
    func='car_park.views.get_data',
    minutes=0.5,
    repeats=-1
)