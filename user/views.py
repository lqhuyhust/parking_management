from .models import Guest, Security, GuestType
from .serializers import GuestSerializer, GuestSingleSerializer, SecuritySerializer, SecuritySingleSerializer, GuestTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.hashers import make_password
# Create your views here.
class GuestList(APIView):
    """
    Just admin has permission to get all guest list and create new guest
    """
    permission_classes = (AllowAny, )
    def get(self, request, format=None):
        if not (self.request.user.is_superuser):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            serializer.save(password=password, is_active=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuestDetail(APIView):
    """
    Guest can get their own information and update it
    Admin has permission to get, update or delete a guest
    """
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        guest = self.get_object(pk)
        print(guest.username)
        if not (self.request.user.id == guest.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = GuestSingleSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guest = self.get_object(pk)
        if not (self.request.user.id == guest.id or self.request.user.is_superuser):
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = GuestSingleSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        if not self.request.user.is_superuser:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SecurityList(APIView):
    """
    Just admin has permission to get all security list and create new security
    """
    permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        securities = Security.objects.all()
        serializer = SecuritySerializer(securities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SecuritySerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            serializer.save(password=password, is_staff=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SecurityDetail(APIView):
    """
    Security can get their own information and update it
    Admin has permission to get, update or delete a security
    """
    def get_object(self, pk):
        try:
            return Security.objects.get(pk=pk)
        except Security.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        security = self.get_object(pk)
        print(security.username)
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = SecuritySingleSerializer(security)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        security = self.get_object(pk)
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = SecuritySingleSerializer(security, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        if not self.request.user.is_superuser:
            return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        security = self.get_object(pk)
        security.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GuestTypeList(generics.ListCreateAPIView):
    """
    Just admin has permission to get all guest type list and create new guest type
    """
    permission_classes = (IsAdminUser, )
    queryset = GuestType.objects.all()
    serializer_class = GuestTypeSerializer


class GuestTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Just admin has permission to get, update or delete a guest type
    """
    permission_classes = (IsAdminUser, )
    queryset = GuestType.objects.all()
    serializer_class = GuestTypeSerializer
