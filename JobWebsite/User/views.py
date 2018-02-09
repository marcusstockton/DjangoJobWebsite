from Attachment.models import Attachment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm, CustomUserCreationForm
from .models import User


def user_list(request):
    queryset_list = User.objects.select_related()

    context = {
        "title": "List",
        "users_list": queryset_list,
    }
    return render(request, "users/index.html", context)


def user_detail(request, pk=None):
    user = get_object_or_404(User.objects.select_related(), pk=pk)
    context = {
        "title": user.username,
        "user": user,
    }
    return render(request, "users/detail.html", context)


def user_edit(request, pk=None):
    instance = get_object_or_404(User.objects.select_related(), pk=pk)
    form = UserForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)

        if request.FILES is not None and len(request.FILES) > 0:
            attachments = Attachment.objects.get(id=instance.attachment_id)
            if form.cleaned_data['avatar']:
                attachments.avatar.delete()
                attachments.avatar = form.cleaned_data['avatar']
            if form.cleaned_data['cv']:
                attachments.cv.delete()
                attachments.cv = form.cleaned_data['cv']
            if form.cleaned_data['avatar'] or form.cleaned_data['cv']:
                attachments.save()

        instance.save()
        messages.success(request, "Successfully Updated")

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
        user = User.objects.create_user(username=username, email=email, password=password, 
                                        first_name=firstname, last_name=lastname, 
                                        birth_date=date_of_birth)

        # Save the files off:
        if request.FILES is not None:
            att = Attachment.objects.create(
                avatar= request.FILES['avatar'] if 'avatar' in request.FILES else None,
                cv= request.FILES['cv'] if 'cv' in request.FILES else None,
                User=user)

        user.save()
        att.save()

        return HttpResponseRedirect(user.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "users/create.html", context)
