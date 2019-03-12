import django_tables2 as tables
from django_tables2.utils import A
from .models import Company

class CompanyTable(tables.Table):
    view = tables.LinkColumn('companies:detail', text='View', args=[A('pk')], orderable=False)
    edit = tables.LinkColumn('companies:edit', text='Edit', args=[A('pk')], orderable=False)
    delete = tables.LinkColumn('companies:delete', text='Delete', args=[A('pk')], orderable=False)
    class Meta:
        model = Company
        exclude = ['id']