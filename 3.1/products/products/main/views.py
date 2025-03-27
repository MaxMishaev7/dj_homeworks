from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import ProductListSerializer
from .serializers import ProductDetailsSerializer
from .models import Product


# Create your views here.


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serial_products = ProductListSerializer(products, many=True)
    return Response(serial_products.data)

class ProductDetails(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serial_product = ProductDetailsSerializer(product)
        return Response(serial_product.data)


