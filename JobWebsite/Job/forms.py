from datetime import datetime

from django.forms import ModelForm, widgets

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


class JobApplyForm(ModelForm):
		
	def __init__(self, *args, **kwargs):
		super(JobApplyForm, self).__init__(*args, **kwargs)

	class Meta:
		model=JobApplication
		fields = [
			"job",
			# "applicant_cv",
			"applicant",
		]
		# widgets={
		#     'job': forms.TextInput(),
		# 	'applicant': forms.TextInput(),
		# }
		localized_fields = "__all__"
