from django.db import models
from django.contrib import admin

class Customer(models.Model):
    '''A customer'''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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

    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.name


class Transaction(models.Model):
    '''A transaction'''
    delivery_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.delivery_number

class ProdutsPurchased(models.Model):
    '''Products related to a transaction'''
    transaction = models.ForeignKey(Transaction)
    product = models.ForeignKey(Product)
