from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import AddressForm
from .models import Address


@login_required
def address_list(request):
    """ Method that returns all addresses """
    queryset_list = Address.objects.select_related('address_type').all()

    context = {
        "title": "List",
        "object_list": queryset_list,
    }
    return render(request, "address/index.html", context)


@login_required
def address_detail(request, pk=None):
    """ Method for retreiving address details"""
    instance = get_object_or_404(Address, pk=pk)
    context = {
        "title": instance.address_line_1,
        "instance": instance
    }
    return render(request, "address/detail.html", context)


@login_required
def address_edit(request, pk=None):
    """ Method for editing an address """
    instance = get_object_or_404(Address, pk=pk)

    # instance means the form data will be populated
    form = AddressForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Updated")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.address_line_1,
        "instance": instance,
        "form": form,
    }
    return render(request, "address/edit.html", context)


@login_required
def address_delete(request, pk=None):
    """ Method for deleting an existing address """
    instance = get_object_or_404(Address, pk=pk)
    instance.delete()
    messages.success(request, "Sucessfully Deleted")
    return redirect("addresses:list")

    return HttpResponse("<h1>Delete</h1>")


@login_required
def address_create(request):
    """ Method for creating a new address """
    form = AddressForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "address/create.html", context)
