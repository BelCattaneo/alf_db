from django.db import models
from django.contrib import admin
from django.db import IntegrityError

class Customer(models.Model):
    '''A customer'''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    socio = models.CharField(blank=True, default=None, null=True, max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    facebook_username = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        '''Returns name and last name'''
        return str(self.first_name).title() + ' ' + str(self.last_name).title()

    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.full_name()

class Product(models.Model):
    '''A Product'''
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    quantity = models.IntegerField()
    minimum_stock = models.IntegerField()
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def pre_delete(self):
        if len(self.transaction_set.all()) > 0:
          raise IntegrityError("product id: " + self.id +  " has associated transactions")


    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.name


class Transaction(models.Model):
    '''A transaction'''
    delivery_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    pay_date = models.DateField(blank=True, default=None, null=True)
    delivery_date = models.DateField(blank=True, default=None, null=True)
    check_reception = models.BooleanField(default=False )
    payment_reception = models.BooleanField(default=False )
    products = models.ManyToManyField(Product)

    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.delivery_number


class TransactionImage(models.Model):
    '''Images attached to a Transaction'''
    image = models.ImageField(upload_to='transaction_images', blank=True, null=True)
    transaction = models.ForeignKey(Transaction)
    
    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.transaction_images.name

