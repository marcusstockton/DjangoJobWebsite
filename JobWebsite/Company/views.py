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

def vote(request, question_id):
    job = get_object_or_404(Job, pk=question_id)
    try:
        selected_job = job.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Job.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Job/detail.html', {
            'question': question,
            'error_message': "You didn't select a job.",
        })
    else:
        selected_job.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('job:results', args=(job.id,)))