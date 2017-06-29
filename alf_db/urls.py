'''Defines URL patterns for alf_db.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # Index page
    url(r'^$', views.index, name='index'),
    
    # CUSTOMERS
    # Customers page
    url(r'^customers/$', views.customers, name='customers'),
    # Add customer
    url(r'^customers/add_customer/$', views.add_customer, name='add_customer'),
    # Delete customer
    url(r'^customers/delete/(?P<customer_id>\d+)/$', views.delete_customer, name='delete_customer'),
    # Detail page
    url(r'^customers/(?P<customer_id>[0-9]+)/$', views.customer_detail, name='customer_detail'),
    # Edit customer page
    url(r'^customers/edit_customer/(?P<customer_id>[0-9]+)/$', views.edit_customer, name='edit_customer'),
    
    # PRODUCTS
    # Products page
    url(r'^products/$', views.products, name='products'),
    # Add product
    url(r'^products/add_product/$', views.add_product, name='add_product'),
    # Delete product
    url(r'^products/delete/(?P<product_id>\d+)/$', views.delete_product, name='delete_product'),
    # Detail page
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
    # Edit product page
    url(r'^products/edit_product/(?P<product_id>[0-9]+)/$', views.edit_product, name='edit_product'),

    # TRANSACTIONS
    # Transacions page
    url(r'^transactions/$', views.transactions, name='transactions'),
    # Add transaction
    url(r'^transactions/add_transaction/$', views.add_transaction, name='add_transaction'),
    # Delete transaction
    url(r'^transactions/delete/(?P<transaction_id>\d+)/$', views.delete_transaction, name='delete_transaction'),
    # Detail page
    url(r'^transactions/(?P<transaction_id>[0-9]+)/$', views.transaction_detail, name='transaction_detail'),
    # Edit transaction page
    url(r'^transactions/edit_transaction/(?P<transaction_id>[0-9]+)/$', views.edit_transaction, name='edit_transaction'),
    
] 