from Address.models import Address
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.transaction import atomic
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig

# Create your views here.
from .forms import CompanyForm, CompanyEditFormCustom
from .models import Company
from .tables import CompanyTable


@login_required
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
    #queryset_list = Company.objects.all()
    table = CompanyTable(Company.objects.all())
    RequestConfig(request).configure(table)

    context = {
        "title": "List",
        #"object_list": queryset_list
        'table': table
    }
    return render(request, "company/index.html", context)


@login_required
def company_edit(request, pk=None):
    instance = get_object_or_404(Company.objects.select_related(), pk=pk)

    data_dict = {'company_name': instance.company_name,
                 "address_line_1": instance.address.address_line_1,
                 "address_line_2": instance.address.address_line_2,
                 "address_line_3": instance.address.address_line_3,
                 "post_code": instance.address.post_code,
                 "county": instance.address.county,
                 "country": instance.address.country
                 }  # dto

    form = CompanyEditFormCustom(request.POST or None, initial=data_dict)

    if request.POST:
        for key, value in request.POST.items():
            print(key + ": " + value)
    if form.is_valid():
        company_name = form.cleaned_data["company_name"]
        address = {"address_line_1": form.cleaned_data["address_line_1"],
                   "address_line_2": form.cleaned_data["address_line_2"],
                   "address_line_3": form.cleaned_data["address_line_3"],
                   "post_code": form.cleaned_data["post_code"],
                   "county": form.cleaned_data["county"],
                   "country": form.cleaned_data["country"]
                   }

        address_new = Address.objects.get(pk=instance.address_id)
        address_new.address_line_1 = address["address_line_1"]
        address_new.address_line_2 = address["address_line_2"]
        address_new.address_line_3 = address["address_line_3"]
        address_new.post_code = address["post_code"]
        address_new.county = address["county"]
        address_new.country = address["country"]

        instance.company_name = company_name
        with atomic():
            instance.save()
            address_new.save()
        messages.success(request, "Successfully Updated")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.company_name,
        "instance": instance,
        "form": form,
    }
    return render(request, "company/edit.html", context)


@login_required
def company_delete(request, pk=None):
    instance = get_object_or_404(Company, pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("company:list")
