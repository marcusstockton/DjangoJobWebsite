from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Job
import datetime
from User.models import User


class JobResource(resources.ModelResource):

	created_by = fields.Field(column_name='created_by', attribute='created_by', widget=ForeignKeyWidget(User))

	class Meta:
		model = Job
		fields = ['id', 'title', 'content', 'description', 'created_by', 'publish', 'min_salary', 'max_salary']
		
	def __init__(self, *args, **kwargs):
		request = kwargs.pop('request')
		self.created_by = request.user
		super(JobResource, self).__init__(*args, **kwargs)

	def before_import_row(self, row, *args, **kwargs):
		row['created_by'] = self.created_by.id
		row['publish'] = datetime.datetime.strptime(row['publish'], '%d-%m-%Y')

		return super(JobResource, self).before_import_row(row, *args, **kwargs)

