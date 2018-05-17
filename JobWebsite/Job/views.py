import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import JobForm, JobApplyForm
from .models import Job
from Attachment.models import Attachment

def job_list(request):
    queryset_list = Job.objects.all().order_by(
        '-publish').exclude(publish__gt=datetime.datetime.now())

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
        messages.success(request, "Sucessfully Updated")

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
    messages.success(request, "Sucessfully Deleted")
    return redirect("jobs:list")

    return HttpResponse("<h1>Delete</h1>")


@login_required
def job_create(request):
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.timestamp = datetime.datetime.now()
        instance.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "jobs/create.html", context)

@login_required
def job_apply(request, pk=None):
    instance = get_object_or_404(Job, pk=pk)
    current_user = request.user
    current_attachment = Attachment.objects.get(User_id=current_user.id)
    if request.method == 'POST':
        form = JobApplyForm(request.POST or None)
        if form.is_valid():
            # process Form
            messages.success(request, "Sucessfully Created")
            return HttpResponseRedirect("jobs/index.html")
    else:
        form = JobApplyForm(initial={
            'job_title': instance.title,
            'current_attachment': current_attachment.cv,
            'user_email_address': current_user.email
            })
    context = {
        "form": form,
    }
    print(form)
    return render(request, "jobs/apply.html", context)