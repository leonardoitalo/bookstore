from rest_framework import serializers
from product.serializers.product_serializer import ProductSerializer
from product.models import Product


class OrderSeralizer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_Total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    

    class Meta:
        model = Product
        fields = ['product', 'total']