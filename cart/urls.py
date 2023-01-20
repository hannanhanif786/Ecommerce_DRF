from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateOrder.as_view(), name="addorder"),
    path("getorder", views.GetOrder.as_view(), name="getorder"),
    path("getor", views.UserOrder.as_view(), name="getorder"),
    path("getaddress", views.GetAddress.as_view(), name="getorder"),
    path("getorder/<int:pk>/", views.OrderId.as_view(), name="byid"),
]
