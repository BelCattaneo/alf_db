from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Customer
from .forms import CustomerForm


def index(request):
    '''The Home Page'''
    return render(request, 'alf_db/index.html')

def customers(request):
    '''Customers page. Show all customers'''
    customers = Customer.objects.order_by('date_added')
    context = {'customers': customers}
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
            return HttpResponseRedirect(reverse('alf_db:customers'))
    
    context = {'form': form}
    return render(request, 'alf_db/add_customer.html', context)

def delete_customer(request, customer_id):
    '''Deletes a customer'''
    if request.method != "POST":
        raise Http404
    else:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
    return redirect('/customers')

def detail(request, customer_id):
    '''Customer detail page.'''
    customer = Customer.objects.get(id=customer_id)
    context = {'customer':customer}
    return render(request, 'alf_db/detail.html', context)

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