from django.contrib import admin

# Register your models here.
from .models  import Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'phone']

    class Meta:
        models = Doctor

admin.site.register(Doctor,DoctorAdmin)