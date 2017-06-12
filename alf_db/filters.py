import django_filters

from .models import Customer, Product

class CustomersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = ['first_name']

class ProductsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = ['name']