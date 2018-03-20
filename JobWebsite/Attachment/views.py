from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Attachment


@login_required
def attachment_list(request):
    queryset = Attachment.objects.all()

    context = {
        "attachments": queryset
    }
    return render(request, "attachments/index.html", context)


@login_required
class DetailView(generic.DetailView):
    model = Attachment
    template_name = 'attachments/detail.html'


@login_required
class EditView(generic.UpdateView):
    model = Attachment
    fields = ['file_name', 'created_date', 'file_type', 'data']
    template_name = 'attachments/edit.html'


@login_required
class DeleteView(generic.DeleteView):
    model = Attachment
    template_name = 'attachments/delete.html'
