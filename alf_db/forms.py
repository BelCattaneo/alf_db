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
    check_reception = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
    class Meta:
        model = Transaction
        fields = ['delivery_number', 'customer', 'delivery_date', 'check_reception', 'products']
        
        labels = {'delivery_number':'Numero de Envio',
                  'customer': 'Cliente',
                  'delivery_date': 'Fecha de Recepción',
                  'check_reception': 'Recepción de Cheque',
                  'products': 'Products'
        }  
                