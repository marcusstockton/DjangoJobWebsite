from django.contrib import admin

from .models import Address, AddressType
# Register your models here.
admin.site.register(Address)
admin.site.register(AddressType)