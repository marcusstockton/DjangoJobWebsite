from datetime import datetime

from django import forms
from django.contrib import messages
from django.forms import ModelForm, widgets

from Attachment.models import Attachment
from User.models import User

from .models import Job, JobApplication


class JobForm(ModelForm):
	created_by = forms.CharField()
	updated_by = forms.CharField(required=False)
	updated_date = forms.DateField()

	class Meta:
		model = Job
		fields = [
			"title",
			"content",
			"publish",
			
		]
		localized_fields = "__all__"
		widgets = {
			'publish': forms.TextInput(attrs={'class': 'datepicker'}),
		}
	def __init__(self, *args, **kwargs):
		super(JobForm, self).__init__(*args, **kwargs)
		job = kwargs.get('instance')
		created_by = job.created_by.username
		updated_by = job.updated_by.username if job.updated_by else None
		updated_date = job.updated_date
		self.fields['created_by'].initial = created_by
		self.fields['created_by'].disabled = True
		if updated_by is not None:
			self.fields['updated_by'].initial = updated_by
			self.fields['updated_date'].initial = updated_date
			self.fields['updated_date'].disabled = True
		self.fields['updated_by'].disabled = True
		

class JobApplyForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		self.job_id = kwargs.pop('job_id')
		super(JobApplyForm, self).__init__(*args, **kwargs)
		
		current_attachments = Attachment.objects.get(User_id=self.user.id)
		job = Job.objects.get(id=self.job_id)
		user = self.user

		self.fields['applicant_email'].widget.attrs['readonly'] = True
		self.fields['applicant_email'].initial = user.email
		self.fields['job_title'].widget.attrs['readonly'] = True
		self.fields['job_title'].initial = job.title
		self.fields['attachment_cv'].initial = current_attachments.cv

	job_id = forms.HiddenInput()
	job_title = forms.CharField(label="Job Title")
	attachment_cv = forms.FileField(label="Current C.V", widget=forms.ClearableFileInput())
	applicant_email = forms.EmailField(label="Email Address")

	
	def save(self, *args, **kwargs):
		job = Job.objects.get(id=self.job_id)
		user = User.objects.get(username=self.user.username)
		application = JobApplication(
			job=job,
			applicant=user,
			applicant_cv=self.cleaned_data['attachment_cv'].instance,
			job_owner=job.created_by,
			created_by=user)

		application.save()

