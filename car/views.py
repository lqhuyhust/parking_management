from rest_framework import status
from rest_framework import permissions
from .models import Car
from .serialzers import CarSerializer, CarSingleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView

# Create your views here.
class CarList(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        print(request.user.is_staff)
        if request.user.is_staff:
            cars = Car.objects.all()
        else:
            cars = Car.objects.filter(guest_id=request.user.id)
        
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        car = self.get_object(pk)
        if not (self.request.user.id == car.guest.id or self.request.user.is_superuser):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSingleSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not self.request.user.is_superuser:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
