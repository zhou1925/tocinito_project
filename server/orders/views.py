import redis
import json
from .models import Order, Product, OrderItem
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import OrderSerializer, ProductSerializer
from rest_framework import status
from .filters import OrdersFilter


r = redis.Redis(host='localhost',port=6379, db=0, charset="utf-8", decode_responses=True)


@api_view(['POST'])
def create_order(request):
    """ get cart from the frontend and process """
    cart = request.data.get('cart')
    products = json.loads(cart)
    
    try:
        order = Order.objects.create()

        for item in products:
            slug, quantity = item['slug'], item['quantity']
            product = get_object_or_404(Product, slug=slug)
            oi = OrderItem.objects.create(product=product, order=order, quantity=quantity)
    
        order.save()
        return Response({ 'message': f'order {order.id} created' }, status=status.HTTP_200_OK)
    except:
        return Response({ 'message': 'Something went wrong' }, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    """
    get orders or filter by date
    :date_stamp_after=2022-07-02
    :date_stamp_before=2022-07-02
    """
    orders = Order.objects.all()
    filterset = OrdersFilter(request.GET, queryset=orders)

    resPerPage = 100
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)
    count = filterset.qs.count()

    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_popular_products(request):
    """
    get popular products from redis
    """
    data = {}
    try:
        products = r.zrevrange('products', 0, -1) # get all products by range
        for index,value in enumerate(products):
            data[index] = value.replace("-", " ")
    except:
        pass
    return Response(data)

@api_view(['GET'])
def get_products(request):
    """ get products """
    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data})
