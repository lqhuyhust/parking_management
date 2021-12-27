from .models import Zone
from.serializers import ZoneSerializer
from rest_framework import generics

# Create your views here.
class ZoneList(generics.ListAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer