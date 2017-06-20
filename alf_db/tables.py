import django_tables2 as tables

from .models import Customer, Product, Transaction

class CustomerTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/customers_actions.html')
    
    class Meta:
        model = Customer

class ProductTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/products_actions.html')
    
    class Meta:
        model = Product

class TransactionTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/transactions_actions.html')
    
    class Meta:
        model = Transaction