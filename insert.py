from fingerprint.models import Emplyee

# create a list of staff objects to be inserted
staff_data = [
    {'staffCode': '1', 'Employeename': 'Aakar Nepal'},
    {'staffCode': '2', 'Employeename': 'Arpana Aryal'},
    {'staffCode': '3', 'Employeename': 'Arun Bhandari'},
    {'staffCode': '4', 'Employeename': 'Basu Budhathoki'},
    {'staffCode': '5', 'Employeename': 'Bijen Chipalu'},
    {'staffCode': '6', 'Employeename': 'Bipan Dhakal'},
    {'staffCode': '7', 'Employeename': 'Davit Khanal'},
    {'staffCode': '8', 'Employeename': 'Devendra Khadka'},
    {'staffCode': '9', 'Employeename': 'Drabin Pokharel'},
    {'staffCode': '10', 'Employeename': 'Gaurav Vasistha'},
    {'staffCode': '11', 'Employeename': 'Hrishi Raj Sonar'},
    {'staffCode': '12', 'Employeename': 'Laxman Tiwari'},
    {'staffCode': '13', 'Employeename': 'Neeroj Bajracharya'},
    {'staffCode': '14', 'Employeename': 'Nitu Tandukar'},
    {'staffCode': '15', 'Employeename': 'Prabina Neupane'},
    {'staffCode': '16', 'Employeename': 'Prakash Bist'},
    {'staffCode': '17', 'Employeename': 'Pramila Tamang'},
    {'staffCode': '18', 'Employeename': 'Rajesh Dulal'},
    {'staffCode': '19', 'Employeename': 'Rohit Chand'},
    {'staffCode': '20', 'Employeename': 'Rupa Deula'},
    {'staffCode': '21', 'Employeename': 'Samyog Mali'},
    {'staffCode': '22', 'Employeename': 'Sanjeev Shrestha'},
    {'staffCode': '23', 'Employeename': 'Sanjiv Shrestha'},
    {'staffCode': '24', 'Employeename': 'Sudaya Maharjan'},
    {'staffCode': '25', 'Employeename': 'Sunita Maharjan'},
    {'staffCode': '26', 'Employeename': 'Suresh Bahadur Chand'},
    {'staffCode': '27', 'Employeename': 'Suresh Kumar Pun Magar'},
    {'staffCode': '28', 'Employeename': 'Swikriti KC'},
    {'staffCode': '29', 'Employeename': 'Tri Narayan Maharjan'},
    {'staffCode': '30', 'Employeename': 'Shreekrishna Ghimire'},
    {'staffCode': '31', 'Employeename': 'Suprim Poudel'},
    {'staffCode': '32', 'Employeename': 'Punam Shah'},
    {'staffCode': '33', 'Employeename': 'Laxmi Menyangbo'},
    {'staffCode': '34', 'Employeename': 'Kopila Chaudhary Tharu'},
    {'staffCode': '35', 'Employeename': 'Ghan Bahadur Pun'},
]

# insert the objects into the database
staff_objects = [Emplyee(**data) for data in staff_data]
Emplyee.objects.bulk_create(staff_objects)
