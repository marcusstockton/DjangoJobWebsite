import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django_tables2 import RequestConfig
from tablib import Dataset
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import JobApplyForm, JobForm, JobCreateForm
from .models import Job, JobApplication, JobType, JobCategory, JobKeySkills, JobBenefits, JobPosistion
from .tables import JobTable
from .resources import JobResource


def job_list(request):
	jobs_applied_for = None

	# Don't show jobs where the publish date is greater than now
	queryset_list = (Job.objects
				  .prefetch_related('created_by', 'updated_by')
				  .order_by('-publish')
				  .exclude(publish__gt=datetime.datetime.now()))

	table = JobTable(queryset_list, request=request)
	RequestConfig(request, paginate={'per_page': 15}).configure(table)

	context = {
		"title": "List",
		"table": table
	}
	return render(request, "jobs/index.html", context)


def job_detail(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)
	have_applied = None
	if not request.user.is_anonymous:
		query = Q(job_id=pk.hex)
		have_applied = JobApplication.objects.filter(applicant_id = request.user.id).filter(job_id = pk.hex).first()
		if not request.user.is_superuser:
			query.add(Q(job_owner_id = request.user), Q.AND)
		applications = JobApplication.objects.filter(query).count()
	else:
		applications = 0
	context = {
		"title": instance.title,
		"instance": instance,
		"application_count": applications,
		"have_applied": have_applied
	}
	return render(request, "jobs/detail.html", context)


@login_required
@permission_required('job.can_change_job', raise_exception=True)
def job_edit(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)

	# instance means the form data will be populated
	form = JobForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.updated = datetime.datetime.now()
		instance.updated_by = request.user
		instance.save()
		form.save_m2m()
		messages.success(request, "Successfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "jobs/edit.html", context)


@login_required
@permission_required('job.can_delete_job', raise_exception=True)
def job_delete(request, pk=None):
	instance = get_object_or_404(Job, pk=pk)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("jobs:index")

	return HttpResponse("<h1>Delete</h1>")


@login_required
@permission_required('job.can_add_job', raise_exception=True)
def job_create(request):
	form = JobCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.created_by = request.user
		instance.created = datetime.datetime.now()
		instance.save()
		form.save_m2m()
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


@login_required
def job_applications(request, pk=None):
	applicants = JobApplication.objects.filter(job_id=pk.hex, job_owner_id = request.user)

	context = {
		"form": applicants
	}

	return render(request, 'jobs/applications.html', context)


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


class JobTypeList(ListView):
	template_name = 'jobs/jobtype/jobtype_list.html'
	model = JobType
	fields = ['description']
	

class JobTypeDetails(DetailView):
	template_name = 'jobs/jobtype/jobtype_details.html'
	model = JobType
	fields = ['description']

class JobTypeCreate(LoginRequiredMixin, CreateView):
	template_name = 'jobs/jobtype/jobtype_form.html'
	model = JobType
	# Need to add in createdby user
	fields = ['description']
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class JobTypeUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'jobs/jobtype/jobtype_form.html'
	model = JobType
	fields = ['description']

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class JobTypeDelete(LoginRequiredMixin, DeleteView):
	model = JobType
	success_url = reverse_lazy('author-list')



class JobPosistionList(ListView):
	template_name = 'jobs/jobposistion/jobposistion_list.html'
	model = JobPosistion
	fields = ['description']

class JobPosistionDetails(DetailView):
	template_name = 'jobs/jobposistion/jobposistion_list.html'
	model = JobPosistion
	fields = ['description']

class JobPosistionCreate(LoginRequiredMixin, CreateView):
	template_name = 'jobs/jobposistion/jobposistion_form.html'
	model = JobPosistion
	# Need to add in createdby user
	fields = ['description']
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class JobPosistionUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'jobs/jobposistion/jobposistion_form.html'
	model = JobPosistion
	fields = ['description']

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class JobPosistionDelete(LoginRequiredMixin, DeleteView):
	model = JobPosistion
	success_url = reverse_lazy('author-list')




class JobCategoryList(ListView):
	template_name = 'jobs/jobcategory/jobcategory_list.html'
	model = JobCategory
	fields = ['description']

class JobCategoryDetails(DetailView):
	template_name = 'jobs/jobcategory/jobcategory_list.html'
	model = JobCategory
	fields = ['description']

class JobCategoryCreate(LoginRequiredMixin, CreateView):
	template_name = 'jobs/jobcategory/jobcategory_form.html'
	model = JobCategory
	# Need to add in createdby user
	fields = ['description']
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class JobCategoryUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'jobs/jobcategory/jobcategory_form.html'
	model = JobCategory
	fields = ['description']

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class JobCategoryDelete(LoginRequiredMixin, DeleteView):
	model = JobCategory
	success_url = reverse_lazy('author-list')




class JobBenefitsList(ListView):
	template_name = 'jobs/jobbenefits/jobbenefits_list.html'
	model = JobBenefits
	fields = ['description']

class JobBenefitsDetails(DetailView):
	template_name = 'jobs/jobbenefits/jobbenefits_list.html'
	model = JobBenefits
	fields = ['description']

class JobBenefitsCreate(LoginRequiredMixin, CreateView):
	template_name = 'jobs/jobbenefits/jobbenefits_form.html'
	model = JobBenefits
	# Need to add in createdby user
	fields = ['description']
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class JobBenefitsUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'jobs/jobbenefits/jobbenefits_form.html'
	model = JobBenefits
	fields = ['description']

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class JobBenefitsDelete(LoginRequiredMixin, DeleteView):
	model = JobBenefits
	success_url = reverse_lazy('author-list')





class JobKeySkillsList(ListView):
	template_name = 'jobs/jobkeyskills/jobkeyskills_list.html'
	model = JobKeySkills
	fields = ['description']

class JobKeySkillsDetails(DetailView):
	template_name = 'jobs/jobkeyskills/jobkeyskills_list.html'
	model = JobKeySkills
	fields = ['description']

class JobKeySkillsCreate(LoginRequiredMixin, CreateView):
	template_name = 'jobs/jobkeyskills/jobkeyskills_form.html'
	model = JobKeySkills
	# Need to add in createdby user
	fields = ['description']
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class JobKeySkillsUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'jobs/jobkeyskills/jobkeyskills_form.html'
	model = JobKeySkills
	fields = ['description']

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class JobKeySkillsDelete(LoginRequiredMixin, DeleteView):
	model = JobKeySkills
	success_url = reverse_lazy('author-list')
