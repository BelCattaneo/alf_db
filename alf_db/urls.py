'''Defines URL patterns for alf_db.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # Index page
    url(r'^$', views.index, name='index'),
    # Customers page
    url(r'^customers/$', views.customers, name='customers'),
    # Add customer
    url(r'^customers/add_customer/$', views.add_customer, name='add_customer'),
    # Delete customer
    url(r'^customers/delete/(?P<customer_id>\d+)/$', views.delete_customer, name='delete_customer'),
    # Detail page
    url(r'^customers/(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    # Edit customer page
    url(r'^customers/edit_customer/(?P<customer_id>[0-9]+)/$', views.edit_customer, name='edit_customer'),
] 