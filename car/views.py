from rest_framework import status
from .models import Car
from user.models import Guest
from .serialzers import CarSerializer, CarSingleSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class CarDetail(APIView):
    permission_classes = (AllowAny, )
    def get_object(self, username):
        try:
            return Guest.objects.get(username=username).car
        except ObjectDoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        car = self.get_object(username)
        # if not (self.request.user.username == username or self.request.user.is_superuser):
        #     return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSingleSerializer(car)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        username = kwargs.get('username')
        car = self.get_object(username)
        # if not (self.request.user.username == username or self.request.user.is_superuser):
        #     return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = CarSingleSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
