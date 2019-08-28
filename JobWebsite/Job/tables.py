import django_tables2 as tables
from django_tables2.utils import A
from .models import Job, JobApplication
import datetime



class TruncatedTextColumn(tables.Column):
    '''A Column to limit to 100 characters and add an ellipsis'''
    def render(self, value):
        if len(value) > 102:
            return value[0:99] + '...'
        return str(value)


class JobTable(tables.Table):
    view = tables.LinkColumn('jobs:detail', text='View', args=[A('pk')], orderable=False)
    edit = tables.LinkColumn('jobs:edit', text='Edit', args=[A('pk')], orderable=False)
    apply = tables.LinkColumn('jobs:apply', text='Apply', args=[A('pk')], orderable=False)
    content = TruncatedTextColumn(accessor=A('content'))
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
        

