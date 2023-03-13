from rest_framework import serializers

from .models import Attendance


# now creating serializers
# class AttendanceSerializer(serializers.Serializer):
#     class meta:
#         model= Attendance
#         fields=('biometricDbId', 'staffCode', 'attendanceState', 'attendanceDate', 'attendanceTime', 'deviceSerialNumber', 'branchCode')

#     def create(self, validated_data):
#         attendance = Attendance.objects.create(**validated_data)
#         return attendance


    # biometricDbId = serializers.IntegerField()
    # staffCode = serializers.CharField(max_length=20)
    # attendanceState = serializers.CharField(max_length=20)
    # attendanceDate = serializers.DateField()
    # attendanceTime =serializers.TimeField()
    # deviceSerialNumber = serializers.CharField(max_length=20)
    # branchCode = serializers.CharField(max_length=20)
    

    # def createAttend(self, validated_data):
    #     # self.instance = self.create(validated_data)
    #     biometricDbId = validated_data.get('biometricDbId')
    #     staffCode = validated_data.get('staffCode')
    #     attendanceState = validated_data.get('attendanceState')
    #     attendanceDate = validated_data.get('attendanceDate')
    #     attendanceTime = validated_data.get('attendanceTime')
    #     deviceSerialNumber = validated_data.get('deviceSerialNumber')
    #     branchCode = validated_data.get('branchCode')

    #     instance = Attendance.objects.create(**validated_data)
    #     instance.save()
    #     return instance
            # biometricDbId = biometricDbId
            # staffCode = staffCode
            # attendanceState = attendanceState
            # attendanceDate = attendanceDate
            # attendanceTime = attendanceTime
            # deviceSerialNumber = deviceSerialNumber
            # branchCode = branchCode)
            # biometricDbId 
            # staffCode 
            # attendanceState
            # attendanceDate 
            # attendanceTime
            # deviceSerialNumber
            # branchCode


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def save(self, **kwargs):
        biometric_db_id = self.validated_data.get('biometricDbId')
        staff_code = self.validated_data.get('staffCode')
        attendance_state = self.validated_data.get('attendanceState')
        attendance_date = self.validated_data.get('attendanceDate')
        attendance_time = self.validated_data.get('attendanceTime')
        device_serial_number = self.validated_data.get('deviceSerialNumber')
        branch_code = self.validated_data.get('branchCode')
        attendance = Attendance(
            biometricDbId=biometric_db_id,
            staffCode=staff_code,
            attendanceState=attendance_state,
            attendanceDate=attendance_date,
            attendanceTime=attendance_time,
            deviceSerialNumber=device_serial_number,
            branchCode=branch_code
        )
        attendance.save()
        return attendance

