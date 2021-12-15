from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Parking, STATUS
from user.models import Guest
from .serializers import ParkingSerializer
from rest_framework.views import APIView

class ParkingList(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        parkings = Guest.objects.get(username=username).parking.all().filter(status='Completed')
        
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

