from django.shortcuts import render
from django.views import generic

from .models import Attachment


def attachment_list(request):
    queryset = Attachment.objects.all()# to filter: .filter(User_id=1)
    
    context = {
        "attachments": queryset
    }
    return render(request, "attachments/index.html", context)


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
