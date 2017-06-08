from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Customer


def index(request):
    '''The Home Page'''
    return render(request, 'alf_db/index.html')

def customers(request):
    '''Customers page. Show all customers'''
    customers = Customer.objects.order_by('date_added')
    context = {'customers': customers}
    return render(request, 'alf_db/customers.html', context)

def delete_customer(request):
    '''Deletes a customer'''
    return redirect('customers')