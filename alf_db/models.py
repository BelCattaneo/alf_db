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

    def full_name(self, first_name, last_name):
        '''Returns name and last name'''
        return str(first_name).title() + ' ' + str(last_name).title()

    def __str__(self):
        '''Returns a string representation of the model.'''
        return self.full_name(self.first_name, self.last_name)
