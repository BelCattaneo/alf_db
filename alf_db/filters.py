import django_filters

from .models import Customer, Product

class CustomersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = {
            'first_name': ['exact', 'contains'],
            'last_name': ['exact', 'contains'],
            'address': ['exact', 'contains'],
            'phone': ['exact', 'contains'],
            'email': ['exact', 'contains'],
            'facebook_username': ['exact', 'contains'],
            'date_added': ['exact', 'contains', 'date__range']
        }

class ProductsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'contains'],
            'code': ['exact', 'contains'],
            'quantity': ['exact', 'contains'],
            'minimum_stock': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'date_added': ['exact', 'contains', 'date__range']
        }