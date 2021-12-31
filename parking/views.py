from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Parking, STATUS
from user.models import Guest
from .serializers import ParkingSerializer
from rest_framework.views import APIView
import pytz
from django.utils import timezone
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from parking_management import settings


RATE = 0.7
class ParkingList(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        parkings = Guest.objects.get(username=username).parking.all()
        
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

class Report(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        parkings = Parking.objects.filter(car_park_id=pk)

        data = [['No', 'User', 'Slot', 'From', 'To','Fee', 'Venue']]
        i = 1
        total = 0.0
        for parking in parkings:
            row_data = [
                i, 
                parking.user, 
                parking.parking_slot, 
                timezone.localtime(parking.time_start, pytz.timezone(settings.TIME_ZONE)).replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S"), 
                timezone.localtime(parking.time_end, pytz.timezone(settings.TIME_ZONE)).replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S"), 
                round(float(parking.fee), 2), 
                round(float(parking.fee)*RATE, 2)]
            total = total + round(float(parking.fee)*RATE, 2)
            data.append(row_data)
            i = i + 1

        car_park_name = parkings[0].car_park.name
        data.append(['Total', '', '', '', '', '', 'VND ' + str(total)])
        fileName = 'reports/'+ car_park_name +'_report.pdf'
        pdf = SimpleDocTemplate(filename=fileName)
        title_style = ParagraphStyle('title_style',
                           fontName="Helvetica-Bold",
                           fontSize=24,
                           alignment=1,
                           spaceAfter=60)

        header_style = ParagraphStyle('header_style',
                           fontName="Helvetica-Bold",
                           fontSize=18,
                           spaceBefore=15,
                           spaceAfter=30)
        title_text = 'Venue Report 2021 December'
        title = Paragraph(title_text, title_style)
        header_summary_text = 'Summary Venue'
        header_summary = Paragraph(header_summary_text, header_style)
        header_detail_text = 'Detail Venue'
        header_detail = Paragraph(header_detail_text, header_style)
        table = Table(data, colWidths=[1 * cm, 1.5 * cm, 2 * cm, 4 * cm,
                               4* cm, 1 * cm, 2 * cm])
        style = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                       ('BOX',(0,0),(-1,-1),1,colors.black),
                       ('BOX',(0,0),(0,-2),1,colors.black)])
        table.setStyle(style)
        elements = []
        data_summary = [
            ['Parking Record Number', 'Total Vunue'],
            [i-1, 'VND ' + str(total)]
        ]
        table_summary = Table(data_summary, colWidths=[10.5 * cm, 5 * cm])
        table_summary.setStyle(style)
        elements.append(title)
        elements.append(header_summary)
        elements.append(table_summary)
        elements.append(header_detail)
        elements.append(table)
        pdf.build(elements)

        return Response('Success', status=status.HTTP_200_OK)

