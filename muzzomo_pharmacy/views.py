from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncWeek , TruncDay , TruncMonth
from django.db.models import Sum

from prescription.models import PrescriptionItem
from medication.models import Medication
from customer.models import Customer
from doctor.models import Doctor

@login_required(login_url='/')
def home_page(request):
    context = {}
    last_day_income = PrescriptionItem.objects.annotate(day=TruncDay('prescription__date')).values('day').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-day').first()
    
    last_week_income = PrescriptionItem.objects.annotate(week=TruncWeek('prescription__date')).values('week').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-week').first()
    
    last_month_income = PrescriptionItem.objects.annotate(month=TruncMonth('prescription__date')).values('month').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-month').first()

    order_total = PrescriptionItem.objects.all().count()
    medicine_total = Medication.objects.all().count()
    doctor_total = Doctor.objects.all().count()
    customer_total = Customer.objects.all().count()

    context['last_day_income'] = last_day_income['total_income']
    context['last_week_income'] = last_week_income['total_income'] // 2
    context['last_month_income'] = last_month_income['total_income'] // 2

    context['order_total'] = order_total
    context['medicine_total'] = medicine_total
    context['doctor_total'] = doctor_total
    context['customer_total'] = customer_total

    total_income = 0

    prescription_item_object = PrescriptionItem.objects.all()

    for item in prescription_item_object:
        total_income += item.quantity * item.medication.medication_cost

    context['total_income'] = total_income

    return render(request , 'home.html' , context)