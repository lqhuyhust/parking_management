from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChangePasswordSerializer
from django.http import Http404

class ChangePassword(generics.UpdateAPIView):
    """
    Just admin or owner can change password
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

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
