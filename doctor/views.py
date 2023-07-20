from django.shortcuts import render

from django.shortcuts import render

from .models import Doctor
# Create your views here.

def doctor_view(request):
    doctor_object = Doctor.objects.all()
    context = {
        'doctor_object': doctor_object
    }
    return render(request , 'doctor/doctor_view.html' , context)

def add_doctor_view(request):
    return render(request , 'doctor/add_doctor_view.html')