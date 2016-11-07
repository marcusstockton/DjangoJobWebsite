from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Job
from .forms import JobForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'latest_jobs_list'

    def get_queryset(self):
        """Return the last five published jobs."""
        return Job.objects.order_by('-publish')[:5]

class DetailView(generic.DetailView):
    model = Job
    template_name = 'jobs/detail.html'


class EditView(generic.UpdateView):
     model = Job
     fields = ['title', 'content', 'publish']
     template_name = 'jobs/edit.html'
     

class DeleteView(generic.DeleteView):
    model = Job
    template_name = 'jobs/delete.html'
