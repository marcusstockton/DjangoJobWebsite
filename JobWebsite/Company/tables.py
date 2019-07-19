import django_tables2 as tables
from django_tables2.utils import A
from .models import Company
from .forms import get_company_data

class CompanyTable(tables.Table):

    nature_of_business = []
    company_type = []

    nature_of_business = tables.Column(empty_values=())
    company_type = tables.Column(empty_values=())
    view = tables.LinkColumn('companies:detail', text='View', args=[A('pk')], orderable=False)
    edit = tables.LinkColumn('companies:edit', text='Edit', args=[A('pk')], orderable=False)
    delete = tables.LinkColumn('companies:delete', text='Delete', args=[A('pk')], orderable=False)
    
    class Meta:
        model = Company
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(CompanyTable, self).__init__(*args, **kwargs)

        company_data = get_company_data()
        self.nature_of_business = company_data['nature_of_business']
        self.company_type = company_data['company_type']


    def render_nature_of_business(self, record):
        if record.nature_of_business != None:
            return self.nature_of_business[record.nature_of_business]
        else:
            return "-"

    def render_company_type(self, record):
        if record.company_type is not None:
            return self.company_type[record.company_type]
        else:
            return "-"