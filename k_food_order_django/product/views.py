from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



# Serializer structure modified to return same format of Response
class HottestProductsList(APIView): # generic views built inside django
    def get(self, request, format=None):
        products = Product.objects.all()[0:5] # the first five hottest products
        serializer = ProductSerializer(products, many=True)
        serial_lista2 = []
        serial_dict = {
            "id": "null",
            "name": "HOTTEST PRODUCTS",
            "products": serializer.data,
        }        
        serial_lista2.append(serial_dict)
        return Response(serial_lista2)

class AllCategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, category_slug, format=None):
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category)
        serial_lista = [] 
        serial_lista.append(serializer.data)
        return Response(serial_lista)

class ProductDetail(APIView): 
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

""" @api_view(['POST'])
def OrderQtyUpdateByProduct(cart):
 """
""" class ProductUpdate(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)    
 """