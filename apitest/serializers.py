from rest_framework import serializers
from apitest.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "descrizione",
            "prezzo",
            "active"
        )