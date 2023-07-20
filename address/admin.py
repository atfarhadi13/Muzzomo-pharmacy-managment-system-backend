from django.contrib import admin

from .models  import Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):

    list_display = ['city', 'state', 'country']

    class Meta:
        models = Address

admin.site.register(Address,AddressAdmin)