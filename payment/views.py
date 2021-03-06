from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from car_park.models import CarPark
from parking.models import Parking, ParkingSlot
from user.models import Guest
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
import qrcode
import json
import datetime
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from parking.serializers import ParkingSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY
FEE = 10000
data = {}

class Success(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        parking = Parking.objects.get(id=pk)
        parking.status = 'Booked'
        parking.save()

        context = {
            'parking': parking
        }
        return render(request, 'success.html', context)

class Failure(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        parking = Parking.objects.get(id=pk)
        parking.delete()
        
        return render(request, 'failure.html')

class Checkout(APIView):
    def post(self, request, *args, **kwargs):
        time_start = datetime.datetime.strptime(request.POST['time_start'], '%Y-%m-%d %H:%M:%S%z')
        time_end = datetime.datetime.strptime(request.POST['time_end'], '%Y-%m-%d %H:%M:%S%z')
        pk = kwargs.get('pk')
        car_park = CarPark.objects.get(pk=pk)

        time = int(((time_end - time_start).total_seconds())/1800) + 1
        fee = int(FEE) * int(time)

        if Parking.objects.filter(user_id=request.user.id, status='Booked'):
            return JsonResponse({'code': 1, 'message':'You have to book only 1 car park at same time'})
        
        try:
            parking = Parking.objects.filter(user_id=request.user.id, status='Pending')
            parking.delete()
        except Parking.DoesNotExist:
            pass

        try:
            available = ParkingSlot.objects.filter(car_park_id=pk, available=True).first()
        except ParkingSlot.DoesNotExist:
            return JsonResponse({'code': 2, 'message':'There is no available parking slot!'})

        customer = stripe.Customer.create(
            email = request.user.email,
            name = request.user.first_name + ' ' + request.user.last_name
        )

        new_parking = Parking(
            user=Guest.objects.get(pk=request.user.id), 
            car_park=car_park, 
            parking_slot=available,
            status = 'Pending',
            time_start=time_start,
            time_end=time_end,
            fee = fee
        )
        new_parking.save()

        session = stripe.checkout.Session.create(
            customer = customer,
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1KErBsLr4TsqrFknlwInjiuF',
                'quantity': time,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success', kwargs={'pk':str(new_parking.id)})),
            cancel_url=request.build_absolute_uri(reverse('failure', kwargs={'pk':str(new_parking.id)})),
        )
        
        data = {
            'Id': new_parking.id,
            'User': new_parking.user.username,
            'Car park': new_parking.car_park.name,
            'Slot': new_parking.parking_slot.name,
            'From': time_start,
            'To': time_end,
            'Fee': str(fee) + ' VND'
        }
        qr_image = qrcode.make(data)
        qr_offset = Image.new('RGB', (600, 600), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{new_parking.user.username}_qrcode.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        new_parking.qr_code.save(files_name, File(stream), save=True)
        new_parking.qr_code_url = 'qrcode/' + str(files_name)
        qr_offset.close()

        return JsonResponse({
            'code': 3,
            'session_id' : session.id,
            'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
        })

    