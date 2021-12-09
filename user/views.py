from .models import Guest, Security, GuestType
from .serializers import GuestSerializer, GuestSingleSerializer, SecuritySerializer, SecuritySingleSerializer, GuestTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password
# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, format=None):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            serializer.save(password=password, is_active=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GuestDetail(APIView):
    permission_classes = (AllowAny, )
    def get_object(self, username):
        try:
            return Guest.objects.get(username=username)
        except Guest.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        print(request.user)
        username = kwargs.get('username')
        guest = self.get_object(username)
        # if request.user.id == guest.id or request.user.is_superuser:
        #     serializer = GuestSingleSerializer(guest)
        #     return Response(serializer.data)
        # return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = GuestSingleSerializer(guest)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        username = kwargs.get('username')
        guest = self.get_object(username)
        # if not (request.user.id == guest.id or request.user.is_superuser):
        #     return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        serializer = GuestSingleSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        username = kwargs.get('username')
        # if not self.request.user.is_superuser:
        #     return Response('Unauthorized', status=status.HTTP_403_FORBIDDEN)
        guest = self.get_object(username)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SecurityList(APIView):
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
    permission_classes = (IsAdminUser, )
    queryset = GuestType.objects.all()
    serializer_class = GuestTypeSerializer


class GuestTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = GuestType.objects.all()
    serializer_class = GuestTypeSerializer
