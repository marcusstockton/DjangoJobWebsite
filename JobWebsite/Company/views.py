from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

# Create your views here.
from .forms import CompanyForm, CompanyEditForm
from .models import Company

def company_create(request):
	form = CompanyForm(request.POST or None, request.FILES or None)
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
		"title": instance.company_name,
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
	instance = get_object_or_404(Company, pk=pk)
	#form = CompanyForm(request.POST or None, instance = instance)# instance means the form data will be populated
	form = CompanyEditForm(request.POST or None, instance = instance)
	if request.POST:
		fav_col = request.POST["favorite_colors"]
		print(fav_col)
		print(request.POST["company_name"] )
	if form.is_valid():
		# instance = form.save(commit=False)
		# instance.save()
		# messages.success(request, "Sucessfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.company_name,
		"instance" : instance,
		"form": form,
	}
	return render(request, "company/edit.html", context)

def company_delete(request, pk=None):
	instance = get_object_or_404(Company, pk=pk)
	instance.delete()
	messages.success(request, "Sucessfully Deleted")
	return redirect("company:list")

	return HttpResponse("<h1>Delete</h1>")