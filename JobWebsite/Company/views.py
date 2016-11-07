from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Job/index.html'
    context_object_name = 'latest_jobs_list'

    def get_queryset(self):
        """Return the last five published jobs."""
        return Job.objects.order_by('-publish')[:5]

class DetailView(generic.DetailView):
    model = Job
    template_name = 'Job/detail.html'


class ResultsView(generic.DetailView):
    model = Job
    template_name = 'Job/results.html'
