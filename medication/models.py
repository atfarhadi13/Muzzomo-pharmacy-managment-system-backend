from django.db import models

# Create your models here.

class Medication(models.Model):
    medication_code = models.CharField(max_length=200)
    medication_name = models.CharField(max_length=200)
    medication_cost = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return self.medication_name