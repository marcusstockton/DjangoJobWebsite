import django_tables2 as tables
from django_tables2.utils import A
from .models import Job, JobApplication
import datetime

class JobTable(tables.Table):
    view = tables.LinkColumn('jobs:detail', text='View', args=[A('pk')], orderable=False)
    edit = tables.LinkColumn('jobs:edit', text='Edit', args=[A('pk')], orderable=False)
    apply = tables.LinkColumn('jobs:apply', text='Apply', args=[A('pk')], orderable=False)

    class Meta:
        model = Job
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(JobTable, self).__init__(*args, **kwargs)
        request = kwargs.get('request')
        
    def before_render(self, request):
        if not request.user.is_authenticated:
            self.columns.hide('apply')
            self.columns.hide('edit')
        else:
            self.columns.show('apply')
            self.columns.hide('edit')
    