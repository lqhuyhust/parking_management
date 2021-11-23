from rest_framework import status
from .models import Car
from .serialzers import CarSerializer, CarSingleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

# Create your views here.
class CarList(APIView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            cars = Car.objects.all()
        elif self.request.user.role.role == 'Guest':
            cars = Car.objects.get(user=self.request.user.id)
        else:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        if not (self.request.user.role.role == 'Guest' or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    """
    Guest can get their own cars and update it
    Admin has permission to get, update or delete a car
    """
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        car = self.get_object(pk)
        if not (self.request.user.id == car.guest.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSingleSerializer(car)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        car = self.get_object(pk)
        if not (self.request.user.id == car.guest.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSingleSerializer(car, data=request.data)
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
