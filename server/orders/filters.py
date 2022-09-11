from django_filters import rest_framework as filters
from .models import Order
    
class OrdersFilter(filters.FilterSet):
    date_stamp = filters.DateFromToRangeFilter()
                                    
    class Meta:
        model = Order
        fields = ('date_stamp',)