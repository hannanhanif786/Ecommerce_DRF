from dataclasses import fields
from rest_framework import serializers
from .models import Order, OrderItems, ShippingAddress


class OrderItmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItmeSerializer(many=True)
    shipping = ShippingAddressSerializer(many=False)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        orderitems = validated_data.pop("orderitems")
        ship = validated_data.pop("shipping")

        order_instance = Order.objects.create(**validated_data)
        for ord in orderitems:
            OrderItems.objects.create(order=order_instance, **ord)
        ShippingAddress.objects.create(order=order_instance, **ship)
        return order_instance
