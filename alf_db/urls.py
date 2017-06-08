'''Defines URL patterns for alf_db.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # Index Page
    url(r'^$', views.index, name='index'),
    # Customers page
    url(r'^customers/$', views.customers, name='customers'),
] 