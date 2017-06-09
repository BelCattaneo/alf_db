import django_filters

from .models import Customer

class CustomersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = ['first_name']