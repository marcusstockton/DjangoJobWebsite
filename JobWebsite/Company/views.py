from Address.models import Address
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.transaction import atomic
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig

# Create your views here.
from Address.forms import AddressForm

from .forms import CompanyForm, CompanyEditForm
from .models import Company
from .tables import CompanyTable


@login_required
def company_create(request):
	form = CompanyForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.created_by = request.user
		instance.created = datetime.datetime.now()
		instance.save()
		messages.success(request, "Sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "company/create.html", context)


@login_required
def company_detail(request, pk=None):
	instance = get_object_or_404(
		Company.objects.select_related('address'), pk=pk)
	context = {
		"title": instance.company_name,
		"instance": instance
	}
	return render(request, "company/detail.html", context)


@login_required
def company_list(request):
	table = CompanyTable(Company.objects.prefetch_related('created_by', 'updated_by', 'address').order_by("-created_date"))
	RequestConfig(request).configure(table)

	context = {
		"title": "List",
		'table': table
	}
	return render(request, "company/index.html", context)


@login_required
def company_edit(request, pk=None):
	instance = get_object_or_404(Company.objects.select_related("address"), pk=pk)
	form = CompanyEditForm(request.POST or None, instance=instance)
	address_form = AddressForm(request.POST or None, instance=instance.address)

	if form.is_valid() and address_form.is_valid():
		instance = form.save(commit=False)
		instance.updated = datetime.datetime.now()
		instance.updated_by = request.user
		instance.save()
		if address_instance.changed_data:
			address_instance = address_form.save(commit=False)
			address_instance.updated = datetime.datetime.now()
			address_instance.updated_by = request.user
			address_instance.save()
		
		messages.success(request, "Successfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.company_name,
		"instance": instance,
		"form": form,
		"address_form": address_form
	}
	return render(request, "company/edit.html", context)


@login_required
def company_delete(request, pk=None):
	instance = get_object_or_404(Company, pk=pk)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("company:index")
