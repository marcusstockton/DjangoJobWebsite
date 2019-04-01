from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job, JobApplication
from .resources import JobResource

# Register your models here.
admin.site.register(JobApplication)

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
	resource_class = JobResource
	def get_resource_kwargs(self, request, *args, **kwargs):
		""" Passing request to resource obj to control exported fields dynamically """
		return {'request': request}

