import django_filters

from .models import Customer, Product, Transaction

class CustomersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            # 'address': 'icontains'],
            # 'phone': ['icontains'],
            'email': ['icontains'],
            'facebook_username': ['icontains'],
            # 'date_added': ['icontains', 'date__range']
        }

class ProductsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'code': ['icontains'],
            # 'quantity': ['icontains'],
            # 'minimum_stock': ['icontains'],
            'description': ['icontains'],
            # 'date_added': ['icontains', 'date__range']
        }

class TransactionsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Transaction
        fields = {
            'delivery_number': ['icontains'],
            'customer': ['exact'],
            # 'date_added': ['icontains', 'date__range']
        }