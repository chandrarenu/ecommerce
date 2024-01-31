from django_filters import rest_framework as filters
from .models import Product
from rest_framework import filters as f

class ProductFilter(filters.FilterSet):
    class Meta:
        model=Product
        
        # product.objects.filter(price__gt=100price__lt)
        fields={
            'category':['exact'],
            'price':['gt','lt'],
            'quantity':['gt','lt']
        }