from django import forms

from .models import Customer, Product, Transaction  

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
                  'facebook_username': 'Facebook'
        }

# Products Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'quantity', 'minimum_stock', 'description']
        labels = {'name':'Nombre',
                  'code': 'Código',
                  'quantity': 'Cantitad',
                  'minimum_stock': 'Stock Mínimo',
                  'description': 'Descripción'
        }

# Transactions Form
class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['delivery_number', 'customer']
        labels = {'delivery_number':'Numero de Envio',
                  'customer': 'Cliente',
        }  
                