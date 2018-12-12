from datetime import datetime

from django.forms import ModelForm, widgets
from django import forms

from .models import Job, JobApplication


class JobForm(ModelForm):

	class Meta:
		model = Job
		fields = [
			"title",
			"content",
			"publish"
		]
		localized_fields = "__all__"
		widgets = {
			"publish": widgets.SelectDateWidget(
				years=range(datetime.now().year, datetime.now().year + 5),
				attrs=({'style': 'width: 30%; display: inline-block;'})),
		}


class JobApplyForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(JobApplyForm, self).__init__(*args, **kwargs)
		self.fields['applicant_email'].widget.attrs['readonly'] = True
		self.fields['job_title'].widget.attrs['readonly'] = True

	job_id = forms.HiddenInput()
	job_title = forms.CharField(label="Job")
	attachment_cv = forms.FileField(label="Current C.V", widget=forms.ClearableFileInput(),)
	applicant_email = forms.EmailField(label="Email Address")
	change_email = forms.BooleanField(widget=widgets.CheckboxInput(),)
	# need to add in a javascript / typescript / jquery file to do watches and changes on the email field
	