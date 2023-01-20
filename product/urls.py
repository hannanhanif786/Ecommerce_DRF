from django.urls import path
from . import views

urlpatterns = [
    path("category", views.CategoryList.as_view(), name="products"),
    path("product", views.ProductCategoryView.as_view(), name="category"),
    path("addproduct", views.AddProduct.as_view(), name="addproduct"),
    path("search", views.SearchProduct.as_view(), name="addproduct"),
]
