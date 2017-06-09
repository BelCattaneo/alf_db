import django_tables2 as tables

from .models import Customer

class CustomerTable(tables.Table):
    actions = tables.TemplateColumn(template_name='alf_db/actions.html')
    
    class Meta:
        model = Customer