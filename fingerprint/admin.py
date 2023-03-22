from django.contrib import admin
from . models import Attendance, Employee
# Register your models here.
admin.site.register(Attendance)

# for visual in admin pannel
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['biometricDbId', 'staffCode', 'attendanceState', 'attendanceDate', 'attendanceTime', 'deviceSerialNumber', 'branchCode']

admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['staffCode', 'employeeName']