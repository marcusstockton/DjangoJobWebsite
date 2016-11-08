from django.shortcuts import render
from django.views import generic
from .models import User
from django.urls import reverse_lazy


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'latest_users_list'

    def get_queryset(self):
        """Return the last five users."""
        return User.objects.all()

class DetailView(generic.DetailView):
    model = User
    template_name = 'users/detail.html'

class EditView(generic.UpdateView):
     model = User
     fields = ['username', 'first_name', 'last_name', 'birth_date', 'email', 'is_superuser', 'is_staff']
     template_name = 'users/edit.html'
     success_url = reverse_lazy('users:detail', kwargs={'pk': model.id,})


class DeleteView(generic.DeleteView):
    model = User
    template_name = 'users/delete.html'
