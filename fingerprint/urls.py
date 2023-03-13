from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('attendances/', views.attendance_view),
    # another url or route for api to post data
    path('createAttendance/', views.createAttendance),
]
