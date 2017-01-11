from django.forms import ModelForm, extras

from .models import Job
from datetime import datetime


class JobForm(ModelForm):

	class Meta:
		model = Job
		fields = [
			"title",
			"content",
			"publish"
		]
		widgets = {
			"publish": extras.SelectDateWidget(years=range(1900, datetime.now().year), attrs=({'style': 'width: 30%; display: inline-block;'})),
		}