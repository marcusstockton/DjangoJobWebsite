from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import AddressForm, AddressEditForm
from .models import Address


def address_list(request):
    queryset_list = Address.objects.all()

    context = {
        "title": "List",
        "object_list": queryset_list,
     }
    return render(request, "address/index.html", context)


def address_detail(request, pk=None):
    instance = get_object_or_404(Address, pk=pk)
    context = {
        "title": instance.address_line_1,
        "instance": instance
    }
    return render(request, "address/detail.html", context)

     
def address_edit(request, pk=None):
    instance = get_object_or_404(Address, pk=pk)
    
    form = AddressEditForm(request.POST or None, instance = instance)# instance means the form data will be populated
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Updated")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.address_line_1,
        "instance" : instance,
        "form": form,
    }
    return render(request, "address/edit.html", context)


def address_delete(request, pk=None):
    instance = get_object_or_404(Address, pk=pk)
    instance.delete()
    messages.success(request, "Sucessfully Deleted")
    return redirect("addresses:list")

    return HttpResponse("<h1>Delete</h1>")


def address_create(request):
    form = AddressForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }# TODO Create create.html page in address templates
    return render(request, "address/create.html", context)