import django_tables2 as tables

from .models import Customer, Product, Transaction

class CustomerTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/customers_actions.html', verbose_name='Acciones')
    first_name = tables.Column(verbose_name='Nombre')
    last_name = tables.Column(verbose_name='Apellido')
    socio = tables.Column(verbose_name='Número de Socio')
    address = tables.Column(verbose_name='Dirección')
    phone = tables.Column(verbose_name='Teléfono')
    email = tables.Column(verbose_name='Mail')
    facebook_username = tables.Column(verbose_name='Facebook')
    date_added = tables.DateColumn(verbose_name='Fecha de Creación')

    class Meta:
        model = Customer
        

class ProductTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/products_actions.html',verbose_name='Acciones')
    name = tables.Column(verbose_name='Nombre')
    code = tables.Column(verbose_name='Código')
    quantity = tables.Column(verbose_name='Cantidad')
    minimum_stock = tables.Column(verbose_name='Stock Mínimo')
    description = tables.Column(verbose_name='Descripción')
    date_added = tables.DateColumn(verbose_name='Fecha de Creación')

    class Meta:
        model = Product

class TransactionTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/transactions_actions.html',verbose_name='Acciones')
    delivery_number = tables.Column(verbose_name='Numero de Envio')
    customer = tables.Column(verbose_name='Cliente')
    pay_date = tables.Column(verbose_name='Fecha de Pago')
    delivery_date = tables.DateColumn(verbose_name='Fecha de Recepción')
    check_reception = tables.BooleanColumn(verbose_name='Recepción de Cheque')
    date_added = tables.DateColumn(verbose_name='Fecha de Creación')
    class Meta:
        model = Transaction