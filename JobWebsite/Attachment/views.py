from django.shortcuts import render
from django.views import generic

from .models import Attachment


class IndexView(generic.ListView):
    template_name = 'attachments/index.html'
    context_object_name = 'latest_attachments_list'

    def get_queryset(self):
        """Return the last five published jobs."""
        return Attachment.objects.order_by('-created_date')[:5]


class DetailView(generic.DetailView):
    model = Attachment
    template_name = 'attachments/detail.html'


class EditView(generic.UpdateView):
    model = Attachment
    fields = ['file_name', 'created_date', 'file_type', 'data']
    template_name = 'attachments/edit.html'
     

class DeleteView(generic.DeleteView):
    model = Attachment
    template_name = 'attachments/delete.html'
