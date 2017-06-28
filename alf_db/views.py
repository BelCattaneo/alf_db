from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from django_tables2 import RequestConfig
from django.db.models import F
from django.contrib import messages

import json

from .models import Customer, Product, Transaction
from .forms import CustomerForm, ProductForm, TransactionsForm
from .tables import CustomerTable, ProductTable, TransactionTable
from .filters import CustomersFilter, ProductsFilter, TransactionsFilter
from datetime import datetime, timedelta

def index(request):
    '''The Home Page'''
    return redirect('/customers')

#---------------------
# CUSTOMERS
#---------------------

def customers(request):
    '''Customers page. Show all customers'''
    
    # Data for the table rendering with django_tables2
    customers_query = Customer.objects.all()
    
    filter = CustomersFilter(request.GET, queryset=customers_query)

    table = CustomerTable(filter.qs)
    RequestConfig(request, paginate={'per_page':10}).configure(table)

    customers_filter_fields = CustomersFilter.Meta.fields

    context = {
      'table': table,
      'filter': filter
    }
    
    return render(request, 'alf_db/customers.html', context)

def add_customer(request):
    '''Adds a customer'''
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = CustomerForm()
    else:
        # POST data submitted; process data.
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente se agregó correctamente!')
            return HttpResponseRedirect(reverse('alf_db:customers'))
        else:
            messages.warning(request, 'Completar correctamente el formulario')

    context = {'form': form}
    return render(request, 'alf_db/add_customer.html', context)

def delete_customer(request, customer_id):
    '''Deletes a customer'''
    if request.method != "POST":
        raise Http404
    else:
        customer = Customer.objects.get(id=customer_id)
        try:
            customer.delete()
        except:
             messages.error(request, 'No se puede borrar el cliente debido a que tiene transacciones asociadas.')

    return redirect('/customers')

def customer_detail(request, customer_id):
    '''Customer detail page.'''
    customer = Customer.objects.get(id=customer_id)
    
    customer_transactions_query = Transaction.objects.all().filter(customer_id=customer_id)
    
    filter = TransactionsFilter(request.GET, queryset=customer_transactions_query)

    table = TransactionTable(filter.qs)
    
    context = {'customer':customer,
               'table': table
    }
    return render(request, 'alf_db/customer_detail.html', context)

def edit_customer(request, customer_id):
    '''Customer edit page'''
    customer = Customer.objects.get(id=customer_id)
    
    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = CustomerForm(instance=customer)
    else:
        # POST data submitted; process data.
        form = CustomerForm(instance=customer, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/customers')
    
    context = {'form': form, 'customer': customer}
    return render(request, 'alf_db/edit_customer.html', context)

#---------------------
# PRODUCTS
#---------------------

def products(request):
    '''Products page. Show all products'''
    
    # Data for the table rendering with django_tables2
    products_query = Product.objects.all()
    
    alert_products = products_query.filter(minimum_stock__gt=F('quantity'))
    filter = ProductsFilter(request.GET, queryset=products_query)

    table = ProductTable(filter.qs)
    RequestConfig(request, paginate={'per_page':10}).configure(table)

    products_filter_fields = ProductsFilter.Meta.fields

    context = {'table': table,
               'filter': filter,
               'alert_products': alert_products,
               'products_filter_fields': json.dumps(products_filter_fields)
    }
    
    return render(request, 'alf_db/products.html', context)

def add_product(request):
    '''Adds a product'''
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = ProductForm()
    else:
        # POST data submitted; process data.
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se agregó correctamente!')
            return HttpResponseRedirect(reverse('alf_db:products'))
    
    context = {'form': form}
    return render(request, 'alf_db/add_product.html', context)

def delete_product(request, product_id):
    '''Deletes a product'''
    if request.method != "POST":
        raise Http404
    else:
        product = Product.objects.get(id=product_id)
        try:
            product.pre_delete()
            product.delete()
        except:
            messages.error(request, 'No se puede borrar el cliente debido a que tiene transacciones asociadas.')

    return redirect('/products')

def product_detail(request, product_id):
    '''Products detail page.'''
    product = Product.objects.get(id=product_id)
    context = {'product':product}
    return render(request, 'alf_db/product_detail.html', context)

def edit_product(request, product_id):
    '''Products edit page'''
    product = Product.objects.get(id=product_id)
    
    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = ProductForm(instance=product)
    else:
        # POST data submitted; process data.
        form = ProductForm(instance=product, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/products')
    
    context = {'form': form, 'product': product}
    return render(request, 'alf_db/edit_product.html', context)

#---------------------
# TRANSACTIONS
#---------------------

def transactions(request):
    '''Transactions page. Show all transactions'''
    
    # Data for the table rendering with django_tables2
    transactions_query = Transaction.objects.all()
    today = datetime.now()
    delta = timedelta(days=15)
    alert_date = today - delta

    check_reception_filter = transactions_query.filter(check_reception=False)

    alert_transactions = check_reception_filter.filter(delivery_date__lt=(alert_date))
    filter = TransactionsFilter(request.GET, queryset=transactions_query)

    table = TransactionTable(filter.qs)
    RequestConfig(request, paginate={'per_page':10}).configure(table)

    transactions_filter_fields = TransactionsFilter.Meta.fields

    context = {
      'table': table,
      'filter': filter,
      'alert_transactions': alert_transactions, 
    }
    
    return render(request, 'alf_db/transactions.html', context)

def add_transaction(request):
    '''Adds a transaction'''
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TransactionsForm()
    else:
        # POST data submitted; process data.
        form = TransactionsForm(request.POST) 

        if form.is_valid():
            form.save()
            messages.success(request, 'La transacción se agregó correctamente!')
            return HttpResponseRedirect(reverse('alf_db:transactions'))


    context = {'form': form}
    return render(request, 'alf_db/add_transaction.html', context)

def delete_transaction(request, transaction_id):
    '''Deletes a transaction'''
    if request.method != "POST":
        raise Http404
    else:
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.delete()
    return redirect('/transactions')

def transaction_detail(request, transaction_id):
    '''Transaction detail page.'''
    transaction = Transaction.objects.get(id=transaction_id)
    
    context = {'transaction':transaction}

    return render(request, 'alf_db/transaction_detail.html', context)

def edit_transaction(request, transaction_id):
    '''Transactions edit page'''
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = TransactionsForm(instance=transaction)
    else:
        # POST data submitted; process data.
        form = TransactionsForm(instance=transaction, data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('/transactions')
    
    context = {'form': form, 'transaction': transaction}
    return render(request, 'alf_db/edit_transaction.html', context)