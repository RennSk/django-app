from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from apitest.models import Product
from apitest.serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]