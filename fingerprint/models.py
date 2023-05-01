from django.db import models

# creating models to store data
class Employee(models.Model):
    staffCode = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.staffCode}, {self.employeeName}"

class Attendance(models.Model):
    biometricDbId = models.IntegerField()
    staffCode = models.CharField(max_length=20)
    attendanceState = models.CharField(max_length=20)
    attendanceDate = models.DateField()
    attendanceTime = models.TimeField()
    deviceSerialNumber = models.CharField(max_length=20)
    branchCode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.biometricDbId}, {self.staffCode}, {self.attendanceState}, {self.attendanceDate}, {self.attendanceTime}, {self.deviceSerialNumber}, {self.branchCode}"
