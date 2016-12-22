from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from Attachment.models import handle_uploaded_file
from .forms import UserForm, CustomUserCreationForm, UserLoginForm
from .models import User


def user_list(request):
    queryset_list = User.objects.all()

    context = {
        "title": "List",
        "users_list": queryset_list,
    }
    return render(request, "users/index.html", context)


def user_detail(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    context = {
        "title": user.username,
        "user": user
    }
    return render(request, "users/detail.html", context)


def user_edit(request, pk=None):
    instance = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Updated")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.username,
        "instance": instance,
        "form": form,
    }
    return render(request, "users/edit.html", context)


def user_delete(request, pk=None):
    instance = get_object_or_404(User, pk=pk)
    instance.delete()
    messages.success(request, "Sucessfully Deleted")
    return redirect("users:list")

    return HttpResponse("<h1>Delete</h1>")


def user_create(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        date_of_birth = form.cleaned_data['birth_date']
        firstname = form.cleaned_data['first_name']
        lastname = form.cleaned_data['last_name']
        email = form.cleaned_data['email']

        # Now save it all off to the database
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                        last_name=lastname, birth_date=date_of_birth)
        user.save()
        messages.success(request, "Sucessfully Created")
        return HttpResponseRedirect(user.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "users/create.html", context)
