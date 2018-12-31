import datetime

from Attachment.forms import AttachmentForm
from Attachment.models import Attachment as attachment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import JobForm, JobApplyForm
from .models import Job, JobApplication


def job_list(request):
    jobs_applied_for = None
    if request.user.is_authenticated:
        jobs_applied_for = JobApplication.objects.filter(applicant=request.user).all()
    
    queryset_list = Job.objects.all().order_by(
        '-publish').exclude(publish__gt=datetime.datetime.now())

    if jobs_applied_for is not None:
        queryset_list.exclude(id__in=jobs_applied_for)

    paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')

    context = {
        "title": "List",
        "object_list": paginator.get_page(page),
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
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.timestamp = datetime.datetime.now()
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "jobs/create.html", context)


@login_required
def job_apply(request, pk=None):
    form = JobApplyForm(request.POST or None, request.FILES or None, user = request.user, job_id = pk or None)
    if form.is_valid():
        form.save(request.FILES or None)
        messages.success(request, "Successfully Applied")
        return HttpResponseRedirect(reverse("jobs:index"))
    
    context = {
        "form": form
    }

    return render(request, "jobs/apply.html", context)
