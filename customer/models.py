from django.db import models

from address.models import Address
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    note = models.TextField()
    address = models.ForeignKey(Address, blank=True, null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + " " + self.last_name