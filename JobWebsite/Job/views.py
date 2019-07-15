import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django_tables2 import RequestConfig
from tablib import Dataset

from .forms import JobApplyForm, JobForm, JobCreateForm
from .models import Job, JobApplication
from .tables import JobTable
from .resources import JobResource


def job_list(request):
	jobs_applied_for = None
	if request.user.is_authenticated:
		jobs_applied_for = JobApplication.objects.filter(
			applicant=request.user).all()

	# Don't show jobs where the publish date is greater than now
	queryset_list = (Job.objects
                  .prefetch_related('created_by', 'updated_by')
                  .order_by('-publish')
                  .exclude(publish__gt=datetime.datetime.now()))

	# Filter out jobs that have been applied for
	if jobs_applied_for is not None:
		queryset_list = queryset_list.exclude(
			id__in=jobs_applied_for.values('job_id'))

	table = JobTable(queryset_list, request=request)
	RequestConfig(request, paginate={'per_page': 10}).configure(table)

	context = {
		"title": "List",
		"table": table
	}
	return render(request, "jobs/index.html", context)


def job_detail(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)
	context = {
		"title": instance.title,
		"instance": instance
	}
	return render(request, "jobs/detail.html", context)


@login_required
def job_edit(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)

	# instance means the form data will be populated
	form = JobForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.updated = datetime.datetime.now()
		instance.updated_by = request.user
		instance.save()
		messages.success(request, "Successfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "jobs/edit.html", context)


@login_required
def job_delete(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("jobs:index")

	return HttpResponse("<h1>Delete</h1>")


@login_required
def job_create(request):
	form = JobCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.created_by = request.user
		instance.created = datetime.datetime.now()
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "jobs/create.html", context)


@login_required
def job_apply(request, pk=None):
	form = JobApplyForm(request.POST or None, request.FILES or None,
	                    user=request.user, job_id=pk or None)
	if form.is_valid():
		existing_record = JobApplication.objects.filter(
			applicant_id=request.user.id.hex, job_id=pk.hex).exists()
		if not existing_record:
			form.save(request.FILES or None)
			messages.success(request, "Successfully Applied")
			return HttpResponseRedirect(reverse("jobs:index"))
		else:
			messages.warning(request, 'Youv\'e already applied for this job.')

	context = {
		"form": form
	}

	return render(request, "jobs/apply.html", context)


def job_import(request):
	if request.method == 'POST' and request.FILES['myfile']:
		job_resource = JobResource(request=request)
		dataset = Dataset()
		new_jobs = request.FILES['myfile']

		imported_data = dataset.load(new_jobs.read())
		result = job_resource.import_data(
			dataset, dry_run=True)  # Test the data import

		if not result.has_errors():
			try:
				data = job_resource.import_data(
					dataset, dry_run=False)  # Actually import now
				if not data.invalid_rows:
					success_message = str(data.total_rows) + " rows inserted"
					messages.success(request, success_message)
				else:
					[print(e) for e in data.invalid_rows()]

			except Exception as err:
				print(err)
		else:
			for err in result.row_errors():
				for e in err[1]:
					error_message = f'{e.error}, {e.row}, {e.traceback}'
					messages.error(request, error_message)
			print(result)

	return render(request, 'jobs/job_import.html')
