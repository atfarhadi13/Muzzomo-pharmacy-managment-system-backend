from django.shortcuts import render

from .models import Customer
# Create your views here.

def customer_view(request):
    customer_object = Customer.objects.all()
    context = {
        'customer_object': customer_object
    }
    return render(request , 'customer/customer_view.html' , context)

def add_customer_view(request):
    return render(request , 'customer/add_customer_view.html')