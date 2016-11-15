from django.views import generic
from .models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm


class IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'latest_users_list'

    def get_queryset(self):
        return User.objects.all()


class DetailView(generic.DetailView):
    model = User
    template_name = 'users/detail.html'


class EditView(generic.UpdateView):
    model = User
    # fields = ['username', 'first_name', 'last_name', 'birth_date', 'email', 'is_superuser', 'is_staff']
    fields = '__all__'
    template_name = 'users/edit.html'
    success_url = reverse_lazy('users:index')


class DeleteView(generic.DeleteView):
    model = User
    template_name = 'users/delete.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "users/create.html"
    success_url = reverse_lazy('users:index')