from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('attendances/', views.attendance_view, name='view_attendance'),
    # another url or route for api to post data
    path('createAttendance/', views.createAttendance),
    # path('flush_table/', views.flush_attendance, name='flush_table'),
]
