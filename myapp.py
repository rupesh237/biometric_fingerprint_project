import json
import requests
URL='http://127.0.0.1:8000/fingerprint/createAttendance/'

data={"data": [{"biometricDbId": 5191, "userId": "1", "attendanceState": "1", "attendanceDate": "2023-03-09", "attendanceTime": "07:25:05", "deviceSerialNumber": "A6F5212160942", "branchCode": "01"}, 
          {"biometricDbId": 5192, "userId": "2", "attendanceState": "1", "attendanceDate": "2023-03-09", "attendanceTime": "07:35:13", "deviceSerialNumber": "A6F5212160942", "branchCode": "01"}, 
          {"biometricDbId": 5193, "userId": "3", "attendanceState": "1", "attendanceDate": "2023-03-09", "attendanceTime": "08:39:33", "deviceSerialNumber": "A6F5212160942", "branchCode": "01"}, 
          {"biometricDbId": 5194, "userId": "4", "attendanceState": "1", "attendanceDate": "2023-03-09", "attendanceTime": "08:46:22", "deviceSerialNumber": "A6F5212160942", "branchCode": "01"}, 
          {"biometricDbId": 5195, "userId": "5", "attendanceState": "1", "attendanceDate": "2023-03-09", "attendanceTime": "08:51:09", "deviceSerialNumber": "A6F5212160942", "branchCode": "01"}]}

# these may be any app written in any languages so we need to
# first convert it into json_data
json_data= json.dumps(data)
r= requests.post(url=URL, data=json_data)