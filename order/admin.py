from django.contrib import admin

from order.models import Order, Discount, OrderHistory


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    pass
