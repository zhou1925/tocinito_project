from rest_framework import serializers
from .models import Order, OrderItem, Product
    
class ProductSerializer(serializers.ModelSerializer):                                    
    class Meta:
        model = Product
        fields = ['title', 'slug', 'price', 'description', 'image' ]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(read_only=True, many=True)
    #date_stamp = serializers.DateField(format="%Y-%m-%d") or DatetimeField %Y-%m-%d %H:%M:%S
    time_stamp = serializers.TimeField(format="%H:%M:%S")
    
    class Meta:
        model = Order
        fields = ['id','items', 'date_stamp', 'time_stamp', 'total', 'total_items']
