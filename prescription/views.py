from django.shortcuts import render

from django.shortcuts import render

from .models import *
from payment.models import *
# Create your views here.

def order_view(request):
    order_object = PrescriptionItem.objects.all()
    context = {
        'order_object': order_object
    }
    return render(request , 'order/order_view.html' , context)

def add_order_view(request):
    return render(request , 'order/add_order_view.html')