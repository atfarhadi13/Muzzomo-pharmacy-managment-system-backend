from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_name = models.CharField(max_length=150)
    note = models.TextField(null=True, blank=True , default='Sold for cost')

    def __str__(self):
        return self.payment_name