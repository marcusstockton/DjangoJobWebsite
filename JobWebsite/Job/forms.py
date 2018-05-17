from django import forms
from django.forms import ModelForm, widgets, Form
from django.utils.safestring import mark_safe

from .models import Job
from Attachment.models import Attachment
from datetime import datetime

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
			"publish": widgets.SelectDateWidget(years=range(datetime.now().year, datetime.now().year + 5), attrs=({'style': 'width: 30%; display: inline-block;'})),
		}

class JobApplyForm(forms.Form):
	attachment = forms.FileField()
	job_title = forms.CharField(disabled=True)
	current_attachment = forms.CharField(max_length=500, disabled=True)
	user_email_address = forms.EmailField(disabled=True)

	def clean_attachment(self):
		attachment = self.cleaned_data['attachment']
		return attachment
	