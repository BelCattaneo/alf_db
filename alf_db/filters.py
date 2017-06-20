import django_filters

from .models import Customer, Product, Transaction

class CustomersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = {
            'first_name': ['contains'],
            'last_name': ['contains'],
            # 'address': 'contains'],
            # 'phone': ['contains'],
            'email': ['contains'],
            'facebook_username': ['contains'],
            # 'date_added': ['contains', 'date__range']
        }

class ProductsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {
            'name': ['contains'],
            'code': ['contains'],
            # 'quantity': ['contains'],
            # 'minimum_stock': ['contains'],
            'description': ['contains'],
            # 'date_added': ['contains', 'date__range']
        }

class TransactionsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {
        }