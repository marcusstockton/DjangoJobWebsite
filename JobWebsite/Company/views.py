from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

# Create your views here.
from .forms import CompanyForm
from .models import Company

# class IndexView(generic.ListView):
#     template_name = 'Job/index.html'
#     context_object_name = 'latest_jobs_list'

#     def get_queryset(self):
#         """Return the last five published jobs."""
#         return Job.objects.order_by('-publish')[:5]

# class DetailView(generic.DetailView):
#     model = Job
#     template_name = 'Job/detail.html'


# class ResultsView(generic.DetailView):
#     model = Job
#     template_name = 'Job/results.html'
def company_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	if not request.user.is_authenticated():
		raise Http404
		
	form = CompanyForm(request.Company or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "company/create.html", context)

def company_detail(request, pk=None):
	instance = get_object_or_404(Company, pk=pk)
	context = {
		"title": instance.title,
		"instance" : instance
	}
	return render(request, "company/detail.html", context)

def company_list(request):
	queryset_list = Company.objects.all()

	context = {
		"title": "List",
		"object_list": queryset_list,
	 }
	return render(request, "company/index.html", context)



def company_edit(request, pk=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Company, pk=pk)
	
	form = CompanyForm(request.Company or None, request.FILES or None, instance = instance)# instance means the form data will be populated
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Sucessfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance" : instance,
		"form": form,
	}
	return render(request, "company/edit.html", context)

def company_delete(request, pk=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404	
	instance = get_object_or_404(Company, pk=pk)
	instance.delete()
	messages.success(request, "Sucessfully Deleted")
	return redirect("company:list")

	return HttpResponse("<h1>Delete</h1>")