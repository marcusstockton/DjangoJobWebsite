from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from .forms import JobForm
from .models import Job


def job_list(request):
    queryset_list = Job.objects.all()

    context = {
        "title": "List",
        "object_list": queryset_list,
     }
    return render(request, "jobs/index.html", context)


def job_detail(request, pk=None):
    instance = get_object_or_404(Job, pk=pk)
    context = {
        "title": instance.title,
        "instance" : instance
    }
    return render(request, "jobs/detail.html", context)

     
def job_edit(request, pk=None):
    instance = get_object_or_404(Job, pk=pk)
    
    form = JobForm(request.POST or None, instance = instance)# instance means the form data will be populated
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
    return render(request, "jobs/edit.html", context)


def job_delete(request, pk=None):
    instance = get_object_or_404(Job, pk=pk)
    instance.delete()
    messages.success(request, "Sucessfully Deleted")
    return redirect("jobs:list")

    return HttpResponse("<h1>Delete</h1>")


def job_create(request):
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "jobs/index.html", context)