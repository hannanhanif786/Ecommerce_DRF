from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCategoryView(APIView):
    def post(self,request,format=None):
        data = self.request.data
        category = data['category_id']
        data = Product.objects.filter(category_id = category)
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SearchProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer      
    filter_backends = [SearchFilter]
    search_fields =   ['$name'] 

        
        