from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Order, OrderItems, ShippingAddress
from .serializers import OrderSerializer, ShippingAddressSerializer
from product.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail


class CreateOrder(APIView):
    def post(self, request, format=None):
        data = request.data
        user = self.request.user
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            subject = 'welcome to Maemes-southall '
            message = f'Hi {user}, thank you for ordering in Maemes-southall.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return Response({"msg": "Create"}, status=status.HTTP_201_CREATED)
        return ({"Error": "Not order created"}, serializer.errors)


class UserOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        data = Order.objects.filter(user=user)

        # ship = ShippingAddress.objects.filter(order=data)
        # print("shippppp", data)
        # relative_news = ShippingAddress.objects.filter(
        #     order__id__in=data.Order.all())
        # print(relative_news)
        serilaizer = OrderSerializer(data, many=True)
        return Response(serilaizer.data)


class OrderId(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetOrder(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# class GetAddress()
class GetAddress(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        data = Order.objects.filter(user=user)
        user_details = ShippingAddress.objects.filter(
            order__id__in=data.values_list('id', flat=True))
        serilaizer = ShippingAddressSerializer(user_details, many=True)
        return Response(serilaizer.data)
