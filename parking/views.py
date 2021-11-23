from rest_framework import generics, status
from rest_framework.response import Response
from .models import Parking
from .serializers import ParkingSerializer, ParkingSingleSerializer
from rest_framework.views import APIView

class ParkingList(APIView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            cars = Parking.objects.all()
        elif self.request.user.role.role == 'Guest':
            cars = Parking.objects.get(user=self.request.user.id)
        elif self.request.user.role.role == 'Security':
            cars = Parking.objects.get(car_park=self.request.user.car_park)
        else:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
        
        serializer = ParkingSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        if not (self.request.user.role.role == 'Guest' or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParkingDetail(APIView):
    def get_object(self, pk):
        try:
            return Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        parking = self.get_object(pk)
        if not (self.request.user.id == parking.guest.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        elif not (self.request.user.role.role == 'Security' and parking.car_park == self.request.user.car_park):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = ParkingSingleSerializer(parking)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        parking = self.get_object(pk)
        if not (self.request.user.is_staff or (self.request.user.role.role == 'Security' and parking.car_park == self.request.user.car_park)):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = ParkingSingleSerializer(parking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)