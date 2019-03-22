from Attachment.models import Attachment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig

from .forms import UserForm, CustomUserCreationForm
from .models import User
from .tables import UserTable


@login_required
def user_list(request):
	user_list = User.objects.filter(is_active=True).select_related(
		'attachment').order_by('-last_login')

	query = request.GET.get('q')
	if query:
		user_list = user_list.filter(
			Q(first_name__icontains=query) | Q(last_name__icontains=query))

	paginator = Paginator(user_list, 10)  # Show 10 contacts per page
	user_list.prefetch_related("Attachment")
	page = request.GET.get('page')

	table = UserTable(user_list, request=request)
	RequestConfig(request).configure(table)

	context = {
		"title": "List",
		"users_list": paginator.get_page(page),
		"table": table
	}
	return render(request, "users/index.html", context)


@login_required
def user_detail(request, pk=None):
	instance = get_object_or_404(User, pk=pk)
	try:
		attachment = Attachment.objects.get(User_id=pk)
	except Attachment.DoesNotExist:
		attachment = Attachment()  # send up an empty attachment object
	context = {
		"title": instance.username,
		"user": instance,
		"attachment": attachment
	}
	return render(request, "users/detail.html", context)


@login_required
def user_edit(request, pk=None):
	instance = get_object_or_404(User, pk=pk)
	form = UserForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)

		if request.FILES is not None and len(request.FILES) > 0:
			try:
				attachments = Attachment.objects.get(User_id=pk)
				if attachments:
					if form.cleaned_data['avatar']:
						attachments.avatar.delete()
						attachments.avatar = form.cleaned_data['avatar']
					if form.cleaned_data['cv']:
						attachments.cv.delete()
						attachments.cv = form.cleaned_data['cv']

			except Attachment.DoesNotExist:
				attachments = Attachment()
				attachments.User_id = pk
				if form.cleaned_data['avatar']:
					attachments.avatar = form.cleaned_data['avatar']
				if form.cleaned_data['cv']:
					attachments.cv = form.cleaned_data['cv']
			finally:
				if form.cleaned_data['avatar'] or form.cleaned_data['cv']:
						attachments.save()
						instance.attachment = attachments

		instance.save()
		messages.success(request, "Successfully Updated")

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.username,
		"instance": instance,
		"form": form,
	}
	return render(request, "users/edit.html", context)


@login_required
def user_delete(request, pk=None):
	instance = get_object_or_404(User, pk=pk)
	instance.delete()
	messages.success(request, "Sucessfully Deleted")
	return redirect("users:list")


def user_create(request):
	form = CustomUserCreationForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		user = form.save()
		messages.success(request, 'Account created successfully')
		return HttpResponseRedirect(user.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "users/create.html", context)
