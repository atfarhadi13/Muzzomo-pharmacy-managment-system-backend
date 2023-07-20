from django.db import models

from customer.models import Customer
from doctor.models import Doctor
from payment.models import Payment
from medication.models import Medication
# Create your models here.

class Prescription(models.Model):
    date = models.DateField(auto_now = True)
    note = models.TextField(null=True, blank=True , default='Sold for cost')
    payment_method = models.ForeignKey(Payment , blank=True , null = True , on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, blank=True, null = True , on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor , blank=True, null = True , on_delete=models.SET_NULL)

    def __str__ (self):
        return str(self.date) + " " + str(self.doctor.first_name) + " " + str(self.customer.first_name)

class PrescriptionItem(models.Model):
    quantity = models.IntegerField()
    customer_loan = models.IntegerField(null=True, default=0 , blank=True)
    note = models.TextField(blank=True , null = True , default='Sold for cost')
    prescription = models.ForeignKey(Prescription , on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication , on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.quantity)