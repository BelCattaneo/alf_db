'''Defines URL patterns for alf_db.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # Index page
    url(r'^$', views.index, name='index'),
    # Customers page
    url(r'^customers/$', views.customers, name='customers'),
    # Delete customer
    url(r'^customers/delete/(?P<customer_id>\d+)/$', views.delete_customer, name='delete_customer')
] 