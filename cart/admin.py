from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("createdAt",)


@admin.register(OrderItems)
class OrderadminAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("address",)
