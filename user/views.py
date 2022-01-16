from .models import Guest
from .serializers import GuestSerializer, GuestSingleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.hashers import make_password
# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, format=None):
        data_user = {
            'username': request.data['username'],
            'password': request.data['password'],
            'email': request.data['email'],
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'phone': request.data['phone']
        }
        serializer_user = GuestSerializer(data=data_user)

        if serializer_user.is_valid():
            password = make_password(self.request.data['password'])
            user = serializer_user.save(password=password, is_active=True)
            return Response(serializer_user.data, status=status.HTTP_201_CREATED)
        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
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
