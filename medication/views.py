from django.shortcuts import render

from django.shortcuts import render

from .models import Medication
# Create your views here.

def medicine_view(request):
    medicine_object = Medication.objects.all()
    context = {
        'medicine_object': medicine_object
    }
    return render(request , 'medicine/medicine_view.html' , context)

def add_medicine_view(request):
    return render(request , 'medicine/add_medicine_view.html')