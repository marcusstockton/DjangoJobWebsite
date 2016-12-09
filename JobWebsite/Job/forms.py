from django import forms

from .models import Job
from django.forms.widgets import SelectDateWidget

class JobForm(forms.ModelForm):
	publish = forms.DateField(widget=SelectDateWidget(years=range(1925, 2100), empty_label=("Choose Year", "Choose Month", "Choose Day")))

	class Meta:
		model = Job
		fields = [
			"title",
			"content",
			"publish"
		]