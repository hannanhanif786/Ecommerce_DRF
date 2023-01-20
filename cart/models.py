from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentmethod = models.CharField(max_length=200, null=True, blank=True)
    taxprice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shippingprice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    totalprice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    ispaid = models.BooleanField(default=False, null=True, blank=True)
    isdelivered = models.BooleanField(default=False, null=True, blank=True)
    deliveredat = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.createdAt)


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, related_name="orderitems"
    )
    name = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True, related_name="shipping"
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postel_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.address)
