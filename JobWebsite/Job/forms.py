import datetime

from django import forms
from django.contrib import messages
from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from Attachment.models import Attachment
from User.models import User
from .models import Job, JobApplication, JobType



class JobForm(ModelForm):
	created_by = forms.CharField()
	updated_by = forms.CharField(required=False)
	updated_date = forms.DateTimeField(required=False)

	class Meta:
		model = Job
		fields = [
			"title",
			"content",
			"publish",
			"min_salary",
			"max_salary",
			"job_type",
			"closing_date",
			"category",
			"primary_location",
			"key_skills"		
		]
		localized_fields = "__all__"
		widgets = {
			'publish': forms.TextInput(attrs={'class': 'datepicker', 'autocomplete':'off', 'placeholder': 'dd/mm/yyyy'}),
			'closing_date': forms.TextInput(attrs={'class': 'datepicker', 'autocomplete':'off', 'placeholder': 'dd/mm/yyyy'})
		}

	def __init__(self, *args, **kwargs):
		super(JobForm, self).__init__(*args, **kwargs)
		job = kwargs.get('instance')
		created_by = job.created_by.username
		updated_by = job.updated_by.username if job.updated_by else None
		updated_date = job.updated_date

		self.fields['created_by'].initial = created_by
		self.fields['created_by'].disabled = True
		self.fields['updated_date'].disabled = True
		self.fields['updated_by'].initial = updated_by
		self.fields['updated_date'].initial = updated_date
		self.fields['updated_by'].disabled = True
		self.fields['job_type'].initial = job.job_type
		self.fields['category'].initial = job.category
		self.fields['primary_location'].initial = job.primary_location
		
		self.fields['key_skills'].initial = job.key_skills


	def clean_publish(self):
		data = self.cleaned_data['publish']
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - publish date in past'))
		
		return data
	
	def clean_max_salary(self):
		max_sal = self.cleaned_data['max_salary']
		min_sal = self.cleaned_data['min_salary']
		if max_sal < min_sal:
			raise ValidationError(_('Invalid Salary - max salary cannot be less than min salary'), code="max_salary")
		return max_sal


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

class JobCreateForm(ModelForm):
	class Meta:
			model = Job
			fields = [
				"title",
				"content",
				"publish",
				"min_salary",
				"max_salary",
				"job_type",
				"closing_date",
				"category",
				"primary_location",
				"key_skills"
				
			]
			localized_fields = "__all__"
			widgets = {
				'publish': forms.TextInput(attrs={'class': 'datepicker', 'autocomplete':'off', 'placeholder': 'dd/mm/yyyy'}),
				'closing_date': forms.TextInput(attrs={'class': 'datepicker', 'autocomplete':'off', 'placeholder': 'dd/mm/yyyy'})
			}
	def clean_publish(self):
		data = self.cleaned_data['publish']
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - publish date in past'))
		
		return data

	def clean_max_salary(self):
		max_sal = self.cleaned_data['max_salary']
		min_sal = self.cleaned_data['min_salary']
		if max_sal < min_sal:
			raise ValidationError(_('Invalid Salary - max salary cannot be less than min salary'), code="max_salary")
		return max_sal