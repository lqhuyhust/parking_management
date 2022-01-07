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
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

stripe.api_key = settings.STRIPE_SECRET_KEY
FEE = 10000
data = {}

def success(request):
    parking = Parking.objects.get(user_id=request.user.id, status='Pending')
    parking.status = 'Booked'
    parking.save()

    return JsonResponse(json.loads(parking))

def failure(request):
    parking = Parking.objects.get(user_id=request.user.id, status='Pending')
    parking.delete()
    return JsonResponse({
        'message': 'Payment Fail'
    })

class Checkout(APIView):
    def post(self, request, *args, **kwargs):
        time_start = request.POST['time_start']
        time_end = request.POST['time_end']
        pk = kwargs.get('pk')
        car_park = CarPark.objects.get(pk=pk)

        time = request.query_params.get('time')
        fee = int(FEE) * int(time)

        if Parking.objects.filter(user_id=request.user.id, status__in=['Pending', 'Booked']):
            return Response({'status': 400, 'message':'You have to book only 1 car park at same time'}, status=status.HTTP_400_BAD_REQUEST)
        
        available = ParkingSlot.objects.filter(car_park_id=pk, available=True).first()
        if not available:
            return Response({'status': 404, 'message':'There is no available parking slot!'}, status=status.HTTP_404_NOT_FOUND)

        customer = stripe.Customer.create(
            email = request.user.email,
            name = request.user.first_name + ' ' + request.user.last_name
        )

        session = stripe.checkout.Session.create(
            customer = customer,
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1KErBsLr4TsqrFknlwInjiuF',
                'quantity': time,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('failure')),
        )

        new_parking = Parking(
            user=Guest.objects.get(pk=request.user.id), 
            car_park=car_park, 
            parking_slot=available,
            status = 'Pending',
            fee = fee
        )
        new_parking.save()
        
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
        qr_offset.close()

        return JsonResponse({
            'session_id' : session.id,
            'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
        })

    