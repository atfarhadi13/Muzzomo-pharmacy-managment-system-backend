from django.contrib import admin

from .models import Payment
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):

    list_display = ['payment_name']

    class Meta:
        models = Payment

admin.site.register(Payment , PaymentAdmin)