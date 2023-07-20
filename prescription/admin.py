from django.contrib import admin

from .models  import Prescription , PrescriptionItem
# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):

    list_display = ['date']

admin.site.register(Prescription , PrescriptionAdmin)

class PrescriptionItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']

    class Meta:
        models = PrescriptionItem

admin.site.register(PrescriptionItem , PrescriptionItemAdmin)