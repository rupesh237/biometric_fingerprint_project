from django.db import models
import json
from django.urls import reverse
from rest_framework import status
from requests import Response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.renderers import JSONRenderer
# this below line exempt csrf token for create attendance
from django.views.decorators.csrf import csrf_exempt

from fingerprint.serializers import AttendanceSerializer
# importing attendanceDB to query for extracting data on demand
from .models import Attendance , Employee

# Create your views here.
def hello(request):
    return HttpResponse('Welcome to fingerprint site')

def attendance_view(request):
    attendance_data = Employee.objects.filter(userId__in=Attendance.objects.values_list('userId', flat=True)).annotate(
    attendanceState=models.Subquery(Attendance.objects.filter(userId=models.OuterRef('userId')).values('attendanceState')[:1]),
    attendanceDate=models.Subquery(Attendance.objects.filter(userId=models.OuterRef('userId')).values('attendanceDate')[:1]),
    attendanceTime=models.Subquery(Attendance.objects.filter(userId=models.OuterRef('userId')).values('attendanceTime')[:1]),
).values('employeeName', 'userId', 'attendanceState', 'attendanceDate', 'attendanceTime')
    return render(request, 'fingerprint/attendance.html', {'attendance_data': attendance_data})

@csrf_exempt
def createAttendance(request):
    json_data = request.body
    python_data = json.loads(json_data)
    python_data = python_data['data']
    
    # Check if the data is a single attendance record or a list of records
    if isinstance(python_data, dict):
        # Data is a single record
        attendance_data = [python_data]
    elif isinstance(python_data, list):
        # Data is a list of records
        attendance_data = python_data
    else:
        # Invalid data format
        return Response({'error': 'Invalid data format. Expected a dictionary or list of dictionaries.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Serialize the data and create the attendance records
    serializer = AttendanceSerializer(data=attendance_data, many=True)
    if serializer.is_valid():
        Attendance.objects.all().delete()
        serializer.save()
        # for response to be send to apia
        res = {'msg': 'Data successfully Inserted'}
        # converting respose into json data
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')


# below view flush Attendance table whenever get executed
# def flush_attendance(request):
#     Attendance.objects.all().delete()
#     return redirect(reverse('view_attendance'))
    