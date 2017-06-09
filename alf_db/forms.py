from django import forms

from .models import Customer

# Customers Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'phone', 'email', 'facebook_username']
        labels = {'first_name':'Nombre',
                  'last_name': 'Apellido',
                  'address': 'Dirección',
                  'phone': 'Teléfono',
                  'email': 'E-Mail',
                  'facebook_username': 'Facebook'}