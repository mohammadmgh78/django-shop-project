from django.contrib import admin

from customer.models import Customer, Address, Discount


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass