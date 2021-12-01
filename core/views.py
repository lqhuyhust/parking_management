from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChangePasswordSerializer
import datetime
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings

class AuthLoginWithJWT(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = {
                'token': token,
                'is_superuser': user.is_superuser,
                'is_staff': user.is_staff,
                'username': user.username
            }
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChangePassword(generics.UpdateAPIView):
    """
    Just admin or owner can change password
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, pk):
        try:
            return User.objects.get(username=pk)
        except User.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk, **kwargs):
        self.object = self.get_object(pk)
        if not (self.request.user.id == self.object.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
