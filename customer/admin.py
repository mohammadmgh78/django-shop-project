from django.contrib import admin

from customer.models import Customer, Address, Discount, Staff, Manager


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class DiscountAdmin(admin.ModelAdmin):
    pass



@admin.register(Staff)
class DiscountAdmin(admin.ModelAdmin):
    pass