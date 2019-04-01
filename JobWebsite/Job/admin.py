from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job, JobApplication
from .resources import JobResource

# Register your models here.
admin.site.register(JobApplication)

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    resource_class = JobResource