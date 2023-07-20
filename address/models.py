from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    note = models.TextField()

    def __str__(self):
        return self.city + " " + self.country