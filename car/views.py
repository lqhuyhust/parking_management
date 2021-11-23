from django.db.models.query import QuerySet
from rest_framework import generics
from .models import Car
from .serialzers import CarSerializer, CarSingleSerializer
from car import serialzers

# Create your views here.
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serialzer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serialzer_class = CarSingleSerializer