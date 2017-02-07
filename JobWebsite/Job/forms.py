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
		localized_fields = "__all__"
		widgets = {
			"publish": extras.SelectDateWidget(years=range(datetime.now().year, datetime.now().year + 5), attrs=({'style': 'width: 30%; display: inline-block;'})),
		}