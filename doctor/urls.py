from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('doctor_view' , doctor_view , name="doctor_view"),
    path('add_doctor_view' , add_doctor_view , name="add_doctor_view"),
]